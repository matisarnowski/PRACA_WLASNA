#include <stdio.h>
#include <iostream>

using namespace std;

int main(void){
    int rok;
    char* wyraz;
    printf("Podaj rok, w którym się urodziłeś: \n");
    scanf("%d", &rok);
    printf("I napisz jakiś wyraz w swoim rodzimym języku: ");
    scanf("%s", wyraz);
    rok = 2021 - rok;
    printf("Wyraz w Twoim rodzimym języku, to: %s.\n", wyraz);
    printf("Masz: %d lat.\n", rok);
    printf("Naciśnij <Enter>, aby wyjść.");
    cin.ignore();
    cin.get();
    return 0;
}