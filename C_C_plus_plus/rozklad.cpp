#include <iostream>
#include <math.h>

using namespace std;

int rozloz(int n, int tab[]){
    short index = 0;
    int number = n;
    for (short i = 2; i <= number; i++){
        while (!(n % i)&&(n/i != 1)){
            cout << i << endl;
            tab[index] = i;
            //cout << " " << n << " ";
            n = n/i;
            index++;
        } 
        while (!(n % i)&&(n/i == 1)) {
            cout << i << endl;
            tab[index] = i;
            n = n/i;
        }
        if (n == 1) break;
    }
    return tab[index];
}

int main(void){
    int n;
    cout << "Podaj liczbe do rozlozenia na czynniki pierwsze: " << endl;
    cin >> n;
    int index = (int) sqrt(n);
    int * tab = new int[index];
    tab[index] = rozloz(n, tab);

    short j = 0;
    while (tab[j] <= n && tab[j] != 0){
        cout << "Element tabeli nr : " << j + 1 << " ,to " << tab[j] << endl;
        j++;
    }

    delete [] tab;
    return 0;
}