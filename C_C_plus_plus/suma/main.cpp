#include <iostream>

using namespace std;

int x, y, suma;

int main()
{
    cout << "Program liczy sume dwoch liczb!" << endl;
    cout << "Podaj pierwsza liczbe: " << endl;
    cin >> x;
    cout << "Podaj druga liczbe: " << endl;
    cin >> y;

    suma = x + y;

    cout << "Suma tych dwoch liczb, to: " << suma;

    return 0;
}
