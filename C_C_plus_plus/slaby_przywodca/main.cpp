#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;


int main()
{

int Tablica[20];
srand(time(NULL));

for (int i = 0; i < 20; i++)
{
    Tablica[i] = rand() % 6 + 45;
    cout << Tablica[i] << endl;
}


int n = 20;

int j, ile = 0;
int a;
for (int i = 0; i < n; i++)
{
    if (ile == 0)
  {
    ile++;
    j = i;
  }
  else if (Tablica[i] == Tablica[j])
  {
    ile++;
  }
  else
  {
    ile--;
  }
}
a = Tablica[j];

int licz = 0;
for (int i = 0; i < n; i++)
{
    if (a == Tablica[i])
    {
         licz++;
    }

}

if (licz > (n/a))
cout << "Slaby przywodca ciagu, to " << a;
else
cout << "Nie znalazlem slabego przywodcy ciagu. ";

return 0;
}

