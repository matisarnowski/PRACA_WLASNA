from math import sqrt


def czy_pierwsza(a):
    licznik = 0
    ogr = sqrt(a)
    ogr = int(ogr)

    for i in range(2, ogr + 1):
        if a % i == 0:
            licznik += 1
    return licznik


print("Liczby bliźniacze - takie dwie liczby pierwsze, których różnica wynosi 2. ")

licz_a = int(input("Podaj pierwszą liczbę naturalną: "))
licz_b = int(input("podaj drugą liczbe naturalną: "))
roznica = 0

if czy_pierwsza(licz_a) == 0 and czy_pierwsza(licz_b) == 0:
    roznica = abs(licz_a - licz_b)
    if roznica == 2:
        print(
            "Brawo liczby: ",
            licz_a,
            " i ",
            licz_b,
            " są liczbami bliźniaczymi. Obydwie ponadto są liczbami pierwszymi. ",
        )
    else:
        print(
            "Niestety liczby ",
            licz_a,
            " i ",
            licz_b,
            " to liczby pierwsze, ale nie bliźniacze. ",
        )
elif czy_pierwsza(licz_a) != 0 and czy_pierwsza(licz_b) != 0:
    print("Żadna z tych liczb nie jest liczbą pierwszą. ")
elif czy_pierwsza(licz_a) != 0 and czy_pierwsza(licz_b) == 0:
    print("Tylko liczba: ", licz_b, "jest liczbą pierwszą. ")
elif czy_pierwsza(licz_a) == 0 and czy_pierwsza(licz_b) != 0:
    print("Tylko liczba: ", licz_a, "jest liczbą pierwszą. ")
