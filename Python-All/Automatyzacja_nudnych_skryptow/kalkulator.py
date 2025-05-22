#!/usr/bin/python3


def wybrane_dzialanie():
    print("Wybierz dzialanie jakie chcesz wykonac: ")
    print(
        "0 - dodawanie, 1 - odejmowanie, 2 - mnożenie, 3 - dzielenie, 4 - potęgowanie, 5 - pierwiastkowanie, 6 - reszta z dzielenia, 7 - dzielenie całkowite, 8 - opuszczenie programu "
    )

    while True:
        dzialanie = input("Podaj numer działania: ")
        if dzialanie == "0":
            while True:
                liczba_1 = float(input("Podaj pierwszą liczbę: "))
                liczba_2 = float(input("Podaj drugą liczbę: "))
                if isinstance(liczba_1, float) and isinstance(liczba_2, float) == True:
                    break
            suma = liczba_1 + liczba_2
            suma = str(suma)
            print("Wynik dodawania, to: " + suma)
        elif dzialanie == "1":
            while True:
                liczba_1 = float(input("Podaj pierwszą liczbę: "))
                liczba_2 = float(input("Podaj drugą liczbę: "))
                if isinstance(liczba_1, float) and isinstance(liczba_2, float) == True:
                    break
            roznica = liczba_1 - liczba_2
            roznica = str(roznica)
            print("Wynik odejmowania, to: " + roznica)
        elif dzialanie == "2":
            while True:
                liczba_1 = float(input("Podaj pierwszą liczbę: "))
                liczba_2 = float(input("Podaj drugą liczbę: "))
                if isinstance(liczba_1, float) and isinstance(liczba_2, float) == True:
                    break
            iloczyn = liczba_1 * liczba_2
            iloczyn = str(iloczyn)
            print("Wynik mnożenia, to: " + iloczyn)
        elif dzialanie == "3":
            while True:
                liczba_1 = float(input("Podaj pierwszą liczbę: "))
                liczba_2 = float(input("Podaj drugą liczbę: "))
                if isinstance(liczba_1, float) and isinstance(liczba_2, float) == True:
                    break
            while liczba_2 == 0:
                print("Nie można dzielić przez zero. Podaj jeszcze raz obie liczby: ")
                while True:
                    liczba_1 = float(input("Podaj pierwszą liczbę: "))
                    liczba_2 = float(input("Podaj drugą liczbę: "))
                    if (
                        isinstance(liczba_1, float)
                        and isinstance(liczba_2, float) == True
                    ):
                        break
            iloraz = liczba_1 / liczba_2
            iloraz = str(iloraz)
            print("Wynik dzielenia, to: " + iloraz)
        elif dzialanie == "4":
            while True:
                liczba_1 = float(input("Podaj pierwszą liczbę: "))
                liczba_2 = float(input("Podaj drugą liczbę: "))
                if isinstance(liczba_1, float) and isinstance(liczba_2, float) == True:
                    break
            potega = liczba_1**liczba_2
            potega = str(potega)
            print("Wynik potęgowania, to: " + potega)
        elif dzialanie == "5":
            while True:
                liczba_1 = float(input("Podaj pierwszą liczbę: "))
                liczba_2 = float(input("Podaj drugą liczbę: "))
                if isinstance(liczba_1, float) and isinstance(liczba_2, float) == True:
                    break
            while (liczba_1 < 0 and liczba_2 % 2 == 0) or liczba_2 == 0:
                if liczba_1 < 0 and liczba_2 % 2 == 0:
                    print(
                        "To nie zadziała na liczbach rzeczywistych, aby wyciągnąć pierwiastek stopnia parzystego z liczby ujemnej potrzebowalibyśmy liczb zespolonych. spróbuj jeszcze raz: "
                    )
                    while True:
                        liczba_1 = float(input("Podaj pierwszą liczbę: "))
                        liczba_2 = float(input("Podaj drugą liczbę: "))
                        if (
                            isinstance(liczba_1, float)
                            and isinstance(liczba_2, float) == True
                        ):
                            break
                else:
                    print(
                        "Nie istnieje pierwiastek stopnia zerowego. Spróbuj jeszcze raz: "
                    )
                    while True:
                        liczba_1 = float(input("Podaj pierwszą liczbę: "))
                        liczba_2 = float(input("Podaj drugą liczbę: "))
                        if (
                            isinstance(liczba_1, float)
                            and isinstance(liczba_2, float) == True
                        ):
                            break
            pierwiastek = liczba_1 ** (1 / liczba_2)
            pierwiastek = str(pierwiastek)
            print("Wynik potęgowania, to: " + pierwiastek)
        elif dzialanie == "6":
            while True:
                liczba_1 = float(input("Podaj pierwszą liczbę: "))
                liczba_2 = float(input("Podaj drugą liczbę: "))
                if isinstance(liczba_1, float) and isinstance(liczba_2, float) == True:
                    break
            reszta = liczba_1 % liczba_2
            reszta = str(reszta)
            print("Wynik dzielenia, to: " + reszta)
        elif dzialanie == "7":
            while True:
                liczba_1 = float(input("Podaj pierwszą liczbę: "))
                liczba_2 = float(input("Podaj drugą liczbę: "))
                if isinstance(liczba_1, float) and isinstance(liczba_2, float) == True:
                    break
            while liczba_2 == 0:
                print("Nie można dzielić przez zero. Podaj jeszcze raz obie liczby: ")
                while True:
                    liczba_1 = float(input("Podaj pierwszą liczbę: "))
                    liczba_2 = float(input("Podaj drugą liczbę: "))
                    if (
                        isinstance(liczba_1, float)
                        and isinstance(liczba_2, float) == True
                    ):
                        break
            iloraz_calk = liczba_1 // liczba_2
            iloraz_calk = str(iloraz)
            print("Wynik dzielenia, to: " + iloraz_calk)
        elif dzialanie == "8":
            print("Kończymy działanie programu. ")
            break


print("Oto prosty kalkulator. Instrukcje zaraz ujrzysz ;)")
wybrane_dzialanie()
