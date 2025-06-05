#include <iostream>

using namespace std;

int main()
{
    int x, y, a, b, t;

    cout << "To jest program liczacy najwiekszy wspolny dzielnik." << endl;
    cout << "Podaj pierwsza liczbe: " << endl;
    cin >> x;
    cout << "Podaj druga liczbe: " << endl;
    cin >> y;
    a = x;
    b = y;

    while ( x != 0 )
    {
        if ( x > y )
        {
            t = x;
            x = y;
            y = t;
        }

    y = y - x;
    }
    cout << "NWD liczb " << a << " oraz " << b << ", to " << y << ".";

    return 0;
}
