#include <iostream>

using namespace std;

int main()
{
    int n, i;
    unsigned long long int suma;

    cout << "Program liczy sume szeregu liczb od 1 do n, dla ustalonego n." << endl;
    cout << "Podaj n: " << endl;
    cin >> n;

    suma = 0;

    for (i = 1; i <= n; i++)
    {
        suma = suma + i*i;
    }

    cout << "Szereg rowny jest: " << suma;

    return 0;
}
