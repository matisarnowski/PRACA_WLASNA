#include <iostream>
#include<cmath>
 using namespace std;
 
 int main()
 {
     int czy_pierwsza = 0;
     cout << "Wprowadź liczbę do sprawdzenia, czy jest pierwsza.";
     cin >> czy_pierwsza;
     int pierwiastek = int(sqrt(czy_pierwsza));
     bool jest_pierwsza_czy_nie_jest = true;
     for (int i = 2; i <= pierwiastek; i++){
        if (czy_pierwsza % i == 0){
            jest_pierwsza_czy_nie_jest = false;
        }
    }
    if (jest_pierwsza_czy_nie_jest == true){
        cout << "Liczba jest pierwsza.";
    }else{
        cout << "Liczba nie jest pierwsza.";
    }
     
}
 
