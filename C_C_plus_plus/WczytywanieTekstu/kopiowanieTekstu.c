void kopiowanieTekstu(char line[], char bufor[]){

    int i = 0;
    
    while(line[i] != '\0'){
        bufor[i] = line[i];
        i++;
    }
}