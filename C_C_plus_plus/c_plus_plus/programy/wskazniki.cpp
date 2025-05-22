#include <stdio.h>
#include <iostream>
#include <string.h>
#include<math.h>

using namespace std;

int main(){

    double wsk;
    double *MaxDouble = &wsk;
    wsk = __DBL_MAX__;
    printf("%e \n", wsk); 
    printf("%lu \n", sizeof(double));
    printf("%lu", sizeof(short int));
    char* wskCh;
    wskCh = (char*)MaxDouble;

    for (char i = 0; i <= 7; i++){
        printf("Wartość bajtu %d: %d \n", i + 1, *(wskCh+ i));
        long int wtmp = (long int) (wskCh + i);
        printf("Adres bajtu %d: %ld \n", i + 1, wtmp);
    }

    string napis = "10010001100000011000000110000001100000011000000110000001";
    long double duzaLiczba = 1.0;

    for (short j = 0; j < 56; j++){   
        if (napis[j] == '1'){
            long double exp = 1.0; 
            exp = -1.0 *(exp + (long double) j);
            long double reszta = powl(2.0, exp);
            printf("%Lf ", reszta);
            duzaLiczba = duzaLiczba + reszta;
        }
    }
    printf("\n%Lf\n", duzaLiczba);

    long double duzaLiczba1 = powl(duzaLiczba, 127.0);

    printf("%Lf\n", duzaLiczba1);

    cout << napis[3] << endl;

    return 0;
}
