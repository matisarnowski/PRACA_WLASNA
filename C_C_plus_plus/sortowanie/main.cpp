#include <iostream>

using namespace std;

int getmax(int tab[], int n)
{
    int max = 0;
    while (n > 0)
    {
        if (tab[max] < tab[n])
        {
            max = n;
        }
     --n;
    }

}
int main()
{
    int tab[100];
    int tab_sort[100];
    int i, k, n;

    cout << "Podaj ilosc elementow tablicy!" << endl;
    cin >> n;
    cout << "Podaj poszczegolne elementy. " << endl;
    for (k = 0; k < n; k++)
    {
        cin >> tab[k];
    }

    while (n > 0)
    {
        i = getmax(tab, n - 1);
        --n;
        tab_sort[n] = tab[i];
        tab[i] = tab[n];
    }
    for (k = 0; k < n; k++)
    {
        cout << tab_sort[k];
    }
    return 0;
}
