#include <stdio.h>

void wczytywanieTekstu(char line[]){
    char c;
    int i = 0;

    while((c = getchar()) && c != EOF && c != '\n' && c != '\0'){
        line[i++] = c;
    }
    line[i] = '\0';
}