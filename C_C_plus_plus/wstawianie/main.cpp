#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void InsertSort(int tab[])
{
    int n = 20;
        for (int i = 1; i < n; i++)
        {
            int j = i;
            int element = tab[j];
            while ((j > 0) && tab[j - 1] > element)
            {
                tab[j] = tab[j - 1];
                j--;
            }
         tab[j] = element;
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

InsertSort(tab);

cout << "Posortowana tablica, to: " << endl;

for (int i = 0; i < 20; i++)
{
    cout << tab[i] << endl;
}
    return 0;
}
