#include <stdio.h>
#include "prototypes.h"

#define MAXLENGTH 1000

int main(){

    char line[MAXLENGTH];
    char bufor[MAXLENGTH];
    wczytywanieTekstu(line);
    kopiowanieTekstu(line, bufor);
    wyswietlanieTekstu(bufor);

    return 0;
}