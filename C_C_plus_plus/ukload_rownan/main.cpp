#include <iostream>

using namespace std;

int main()
{
    double a1, a2, b1, b2, c1, c2, WY, WX, W;
    cout << "Ten program liczy rozwiazania ukladu rownan metoda wyznacznikow!" << endl;
    cout << "Wprowadz a1 stojace przy x w pierwszym rownaniu: " << endl;
    cin >> a1;
    cout << "Wprowadz b1 stojace przy y w pierwszym rownaniu: " << endl;
    cin >> b1;
    cout << "Wprowadz c1 stojace po drugiej stronie pierwszego rownania: " << endl;
    cin >> c1;
    cout << "Wprowadz a2 stojace przy x w drugim rownaniu: " << endl;
    cin >> a2;
    cout << "Wprowadz b2 stojace przy y w drugim rownaniu: " << endl;
    cin >> b2;
    cout << "Wprowadz c2 stojace po drugiej stronie drugiego rownania: " << endl;
    cin >> c2;

    WY = a1*c2 - c1*a2;
    WX = c1*b2 - b1*c2;
    W = a1*b2 - b1*a2;

    if (W != 0)
    {
        cout << "Wynik y, to: " << WY/W << endl;
        cout << "Wynik x, to: " << WX/W;
    }
    else
    {
        if ((WY != 0) || (WX != 0))
        {
            cout << "Uklad rownan jest sprzeczny i nie ma rozwiazan." << endl;
        }
        else
        {
            cout << "Uklad rownan jest nieoznaczony i nie ma rozwiazan." << endl;
        }
    }
    return 0;
}
