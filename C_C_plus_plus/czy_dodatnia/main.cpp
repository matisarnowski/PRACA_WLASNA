#include <iostream>

using namespace std;

int main()
{
    int x;
    cout << "Program sprawdza, czy liczba jest dodatnia!" << endl;
    cout << "Podaj liczbe: " << endl;
    cin >> x;

    if (x>0)
    {
        cout << "TAK!" << endl;
    }
    else
    {
        cout << "NIE!" << endl;
    }
    return 0;
}
