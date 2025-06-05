#include <iostream>

using namespace std;

int main()
{
   int Tablica_A[10], Tablica_B[10];
cout << "Wpisz dowolne liczby dla pierwszej tablicy rosnaco: " << endl;
for (int i = 0; i < 10; i++)
{
    cin >> Tablica_A[i];
}
cout << "Wpisz dowolne liczby dla drugiej tablicy rosnaco: " << endl;
for (int i = 0; i < 10; i++)
{
    cin >> Tablica_B[i];
}

 int wynik = 0;
 int i = 0;
 int j = 0;
 while (i < 10)
 if ((j < 10) && Tablica_A[i] > Tablica_B[j])
 {
     j++;
 }
 else
 {
        wynik = wynik + j;
        i++;
 }
 if (wynik < 0)
 {
     wynik = 0;
 }
 else
 cout << "Inwersji jest: " << wynik;
    return 0;
}
