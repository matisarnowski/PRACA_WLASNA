#include <iostream>
using namespace std;


int main(){
    /*to jest pierwszy
    komentarz // drugi
        // trzeci
        // czwarty
    a to dokończenie
    *********************************/
    cout << "To jest progarm do sprawdzania, czy komentarze są poprawne. A więc pierwszy komentarz działa. " << endl;
    // wysokosc = 660; // próba nieudana
    cout << "Drugi komentarz też jest jak najbardziej poprawny. " << endl;
    /* -------------
    szerokosc = 23; // wstępna wartość
    gestosc = 12.55; /* wzięta z tablicy */
    // dalsze oblizenia
    ----------- */
    cout << "Trzeci komentarz jest nie poprawny. Program się nie skompiluje. Po słowie 'tablicy' odczytuje zakończenie komentarza \\
    poprzez znak */ i wszystko, co jest dalej uważa za pełnoprawną część kodu programu tymczasem, to są bzdury. " << endl; 
    return 0;
}