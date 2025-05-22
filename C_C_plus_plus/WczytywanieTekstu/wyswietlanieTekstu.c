#include <stdio.h>

void wyswietlanieTekstu(char bufor[]){

    char c;
    int i = 0;

    while(bufor[i] != '\0'){
        c = bufor[i++];
        printf("%c", c);
    }
    printf("\n");
}