#include <iostream>
#include <limits> // Potrzebne dla std::numeric_limits
#include <string> // Potrzebne dla std::string i std::getline

// Używanie przestrzeni nazw std, aby nie pisać std:: przed cout, cin, endl
using namespace std;

// Funkcja mnozenie0 pozostaje bez zmian
int mnozenie0(int n, int a){
    if ( n == 1 ) return a;
    return mnozenie0(n - 1, a) + a;
}

int main(){
    int n, a;

    cout << "Podaj dwie liczby, które mają być przez siebie pomnożone, najpierw pierwszą potem drugą:" << endl;
    
    // Pętla do wczytywania pierwszej liczby, odporna na błędne dane
    while (!(cin >> n)) {
        cout << "Błędne dane. Proszę podać liczbę całkowitą dla pierwszej wartości: ";
        cin.clear(); // Wyczyść flagi błędu strumienia
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Odrzuć błędne dane wejściowe
    }

    // Pętla do wczytywania drugiej liczby, odporna na błędne dane
    while (!(cin >> a)) {
        cout << "Błędne dane. Proszę podać liczbę całkowitą dla drugiej wartości: ";
        cin.clear(); // Wyczyść flagi błędu strumienia
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Odrzuć błędne dane wejściowe
    }

    cout << "Wynik mnożenia: " << mnozenie0(n, a) << endl;

    // --- DODANA SEKCJA - CZEKANIE NA ENTER ---
    cout << endl; // Dodatkowa nowa linia dla czytelności
    cout << "Naciśnij Enter, aby zakończyć...";
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Wyczyść bufor wejściowy z poprzednich operacji (jeśli coś zostało)
                                                        // Szczególnie ważne, jeśli poprzednie cin >> a; nie pobrało znaku nowej linii
    string dummy_input; // Zmienna do przechwycenia wciśnięcia Enter
    getline(cin, dummy_input); // Czekaj, aż użytkownik wciśnie Enter
    // --- KONIEC DODANEJ SEKCJI ---

    return 0;
}