#include <iostream>
#include <string.h>

using namespace std;

void GetPassword(string *password){
    char pass[20];

    cout << "Wprowadz haslo: " << endl;
    cin.getline(pass, sizeof(pass));
    *password = pass;
} 

int main(){
    int i;
    char str[20];
    string password;
    GetPassword(&password);
    const char* pass_true = password.c_str();

    cout << pass_true << endl;

    for (i = 0; i <= 3 && strcmp(str, pass_true); ++i){
        cout << "Podaj haslo: " << endl;
        cin.getline(str, sizeof(str));

        if (i < 3 && strcmp(str, pass_true)){
            cout << "Niestety podales bledne haslo." << endl;
        }
    }
    if (i == 4){
        cout << "Zbyt duza liczba prob." << endl;
    } else cout << "Jestes zalogowany!" << endl;
    cout << "Nacisnij klawisz <Enter>." << endl;
    cin.get();
    return 0;
}