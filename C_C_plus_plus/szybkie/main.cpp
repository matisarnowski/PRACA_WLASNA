#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void qsort(int tab[], int left, int right)
{
    if(left < right)
    {
        int m = left;
        for (int i = left + 1; i <= right; i++)
        {
            if (tab[i] < tab[left])
                swap(tab[++m], tab[i]);
        }
        swap(tab[left], tab[m]);
        qsort(tab, left, m-1);
        qsort(tab, m+1, right);
    }
}
int main()
{
int tab[20];
srand(time(NULL));

for (int i = 0; i < 20; i++)
{
    tab[i] = rand() % 50 + 1;
    cout << tab[i] << endl;
}

qsort(tab,0,19);

cout << "Posortowana tablica, to: " << endl;

for (int i = 0; i < 20; i++)
{
    cout << tab[i] << endl;
}
    return 0;
}
