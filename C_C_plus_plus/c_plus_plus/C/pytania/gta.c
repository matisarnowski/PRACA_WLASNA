#include <stdio.h> // standardowa biblioteka we/wy
#include <stdlib.h> // standardowa biblioteka dla exit i malloc
#include <string.h> // biblioteka łańcuchów tekstu

struct node {
    struct node *no; // odnosi się do węzła z odpowiedzią 'nie'
    struct node *yes; // odnosi się do węzła z odpowiedzią 'tak'
    char string[1]; // pytanie albo zwierzę
};

struct node *
make_node(char *string)
{
    struct node *memory; //nowo alokowana pamięć

    if ((memory = (struct node *)malloc(sizeof(struct node) + strlen(string))) == (struct node *)0){
        (void)fprintf(stderr, "gta: out of memory.\n");
        exit(-1);
    }

    (void)strcpy(memory->string, string);
    memory->yes = memory->no = (struct node *)0;

    return (memory);
}

int 
main(int argc, char *argv[])
{
    char animal[50]; // bufor na nową nazwę zwierzęcia
    char buffer[3]; // bufor znaków wprowadzanych przez gracza
    int c; // aktualny znak bufora
    struct node **current; // aktualny węzeł na drzewie
    FILE *in; // plik wejściowy do zapisania danych treningowych
    struct node *new; // wskaźnik usuwania znaku nowej linii
    FILE *out; // bufor na nowe pytanie
    char *p; // wskaźnik usuwania znaku nowej linii
    char question[100]; // bufor na nowe pytanie
    struct node *root; // korzeń drzewa wiedzy

    // Przetwarzanie argumentów z wiersza poleceń.

    in = out = (FILE *)0;

    for (argc--, argv++; argc > 1 && argc % 2 == 0; argc -= 2, argv += 2){
        if(strcmp(argv[0], "-i") == 0 && (FILE *)0){
            if((in = fopen(argv[1], "r")) == (FILE *)0){
                (void)fprintf(stderr, "gta: can't open input file '%s'.\n", argv[1]);
                exit(-1);
            }
        }
        else if(strcmp(argv[0], "-o") == 0 && out == (FILE *)0){
            if ((out = fopen(argv[1], "w")) == (FILE *)0){
                (void)fprintf(stderr, "gta: can't open input file '%s.\n", argv[1]);
                exit(-1);
            }
        }
        else break;
    }
    if(argc > 0){
        (void)fprintf(stderr,"usage: gta [-i input-file-name] [-o output-file-name]\n");
        exit(-1);
    }

    // Czytaj ze standardowego wejścia, jeśli żaden pliok wejściowy nie został określony w wierszu poleceń.

    if (in == (FILE *)0) in = stdin;

    // Tworzenie początkowego drzewa wiedzy.

    root = make_node("Czy ono szczeka");
    root->yes = make_node("pies");
    root->no = make_node("kot");

    for(;;){ // Graj w grę dopóki użytkownik z niej nie wyjdzie.
        
        if (in == stdin) 
            (void)printf("Pomyśl o jakimś zwierzęciu.\n");

        current = &root; // Zacznij od góry

        for (;;){ // Graj w grę

            for (;;){
                if (in == stdin){
                    if ((*current)->yes == (struct node *)0) 
                        (void)printf("Czy to ");

                    (void)printf("%s?[ynq] ",(*current)->string);
                }
                
                if (fgets(buffer, sizeof(buffer), in) == (char *)0 || strcmp(buffer,"q\n") == 0){
                    if (in != stdin){
                        (void)fclose(in);
                        in = stdin;
                    }
                    else{
                        if (in == stdin) 
                            (void)printf("\nDzięki za grę. Do zobaczenia. \n");
                        exit(0);
                    }
                }
                else if (strcmp(buffer, "y\n") == 0){
                    if (out != (FILE *)0) fputs("y\n", out);

                    current = &((*current)->yes);

                    if (*current == (struct node *)0){
                        (void)printf("Wiedziałem!\n");
                        break;
                    }
                }
                else if (strcmp(buffer, "n\n") == 0){
                    if (out != (FILE *)0) fputs("n\n", out);

                    if ((* current)->no == (struct node *)0){
                        if (in == stdin) 
                            (void)printf("Poddaję się. Co to za zwierzę? ");

                        fgets(animal, sizeof (animal), in);

                        if(out != (FILE *)0) 
                            fputs (animal, out);

                        if ((p = strchr(animal, '\n')) != (char *)0) 
                            *p = '\0';

                        if (in == stdin)
                            (void)printf("Jakim pytaniem mógłbym odróżnić %s od %s? ", 
                            animal, (*current)->string);
                        fgets(question, sizeof(question), in);

                        if (out != (FILE *)0)
                            fputs (question, out);

                        if ((p = strchr(question, '\n')) != (char *)0)
                            *p = '\0';

                        new = make_node(question);
                        new->yes = make_node(animal);
                        new->no = *current;
                        *current = new;

                        if (in == stdin) 
                            (void)printf("Dzięki! Zapamiętam to zwierzę. \n");

                        break;                    
                    }
                    else current = &((*current)->no);
                }
                else {
                    if (in == stdin) 
                        (void)printf("Co to takiego? Wpisz proszę y za tak, n za nie, lub q aby wyjść. \n");

                    while ((c = getc(in)) != '\n' && c != EOF)
                        ;
                }
            }
            break;
        }
        if (in == stdin) (void)printf("Zagrajmy jeszcze raz.\n\n");
    }
}