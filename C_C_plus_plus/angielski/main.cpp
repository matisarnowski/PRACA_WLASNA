#include <iostream>

using namespace std;

int main()
{
    unsigned short int x;

    cout << "Podaj ilosc zdybytych punktow z testu kwalifikujacedgo do grup jezyka angielskiego! Uzyskasz nazwe grupy. Wartosc musi byc liczba nieujemna." << endl;
    cin >> x;

    if (x <= 29)
        cout << "Podstawowa." << endl;
    else if (x <= 49)
        cout << "Sredniozaawansowana." << endl;
    else if (x <= 70)
        cout << "Zaawansowana." << endl;
    else
        cout << "Blad przekroczono zakres." << endl;

    return 0;
}
