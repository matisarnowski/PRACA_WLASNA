import sys

print(
    "Liczba podzielna - liczba naturalna, która jest większa od 0 i dzieli się przez sumę swoich cyfr."
)

licz = int(input("Wprowadź liczbę do sprawdzenia. "))


if licz > 0:
    spr = licz
    suma = 0
    while spr > 0:
        suma += spr % 10
        spr /= 10
        spr = int(spr)

    if licz % suma == 0:
        print("Liczba ", licz, "jest liczbą podzielną. Suma jej cyfr, to: ", suma)
    else:
        print("Liczba ", licz, " nie jest liczbą podzielną. Suma jej cyfr, to: ", suma)

else:
    print("liczba mniejsz od jednośc, nie może być liczbą podzielną. ")
    sys.exit()
