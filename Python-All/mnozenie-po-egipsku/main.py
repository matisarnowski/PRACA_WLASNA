# Funkcja mnozenie0
def mnozenie0(n, a):
    if n == 1:
        return a
    return mnozenie0(n - 1, a) + a

def main():
    print("Podaj dwie liczby, które mają być przez siebie pomnożone, najpierw pierwszą potem drugą:")

    # Pętla do wczytywania pierwszej liczby, odporna na błędne dane
    while True:
        try:
            n_str = input("Pierwsza liczba: ")
            n = int(n_str)
            break  # Wyjdź z pętli, jeśli konwersja się powiedzie
        except ValueError:
            print("Błędne dane. Proszę podać liczbę całkowitą dla pierwszej wartości.")

    # Pętla do wczytywania drugiej liczby, odporna na błędne dane
    while True:
        try:
            a_str = input("Druga liczba: ")
            a = int(a_str)
            break  # Wyjdź z pętli, jeśli konwersja się powiedzie
        except ValueError:
            print("Błędne dane. Proszę podać liczbę całkowitą dla drugiej wartości.")

    print(f"Wynik mnożenia: {mnozenie0(n, a)}")

    # --- DODANA SEKCJA - CZEKANIE NA ENTER ---
    print()  # Dodatkowa nowa linia dla czytelności
    input("Naciśnij Enter, aby zakończyć...")
    # --- KONIEC DODANEJ SEKCJI ---

if __name__ == "__main__":
    main()