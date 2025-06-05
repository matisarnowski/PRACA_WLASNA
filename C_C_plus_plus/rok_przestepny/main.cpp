#include <iostream>

using namespace std;

int main()
{
    int rok;

    cout << "Podaj rok: " << endl;
    cin >> rok;
    cout << "Czy rok " << rok << " jest przestepny?" <<endl;

    if ((rok % 4 == 0) && (rok % 100 != 0))
    {
        cout << "To jest rok przestepny." << endl;
    }
    else if (rok % 400 == 0)
    {
        cout << "To jest rok przestepny." << endl;

    }
    else
        {
        cout << "To nie jest rok przestepny.";
        }

    return 0;
}
