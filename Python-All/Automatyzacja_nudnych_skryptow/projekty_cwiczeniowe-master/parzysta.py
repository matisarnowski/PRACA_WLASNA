# Czy liczba jest parzysta?

global liczba
458
liczba = int(input("Podaj dowolną liczbę, całkowita: "))


ostatnia = liczba % 10


if ostatnia == 0 or ostatnia == 2 or ostatnia == 4 or ostatnia == 6 or ostatnia == 8:
    print(
        "Liczba ",
        liczba,
        " jest liczbą parzystą, ponieważ jej ostatnia cyfra, to: ",
        ostatnia,
    )
else:
    print(
        "Liczba ",
        liczba,
        " jest liczbą nie parzystą, ponieważ jeje ostatnia cyfra, to: ",
        ostatnia,
    )

if liczba > 1:
    ostatnia = liczba
    while ostatnia > 1:
        ostatnia -= 2

if ostatnia == 0:
    print(
        "Liczba ",
        liczba,
        " jest liczbą parzystą, ponieważ przy konsekwentnym odejmowaniu dwójki, zmienia się w: ",
        ostatnia,
    )
else:
    print(
        "Liczba ",
        liczba,
        " jest liczbą nie parzystą, ponieważ przy konsekwentnym odejmowaniu dwójki, zmienia się w: ",
        ostatnia,
    )
