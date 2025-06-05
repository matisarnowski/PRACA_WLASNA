#include <iostream>
#include "nww.hpp"
using namespace std;

int main(){
 int a, b;
 cout << "Podaj pierwszą wartość, liczbę całkowitą, "
 << "która posłuży do obliczenia największego wspólnego " 
 << "dzielnika i najmniejszej wspólnej wielokrotności\n";
 cin >> a;
 cout << "Podaj drugą wartość.\n";
 cin >> b;
 cin.ignore();

 int dzielnik = nwd(a, b);
 int mnoznik = nww(a, b);
 
 cout << "NWD, to: " << dzielnik << " \na NWW, to: " << mnoznik << "\n";
 cout << "Wciśnij <Enter>, aby zakończyć.\n";
 cin.get();
 return 0;
 }