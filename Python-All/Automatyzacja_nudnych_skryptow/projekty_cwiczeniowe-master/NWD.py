def nwd(a, b):
    if a == 0:
        return b
    while b != 0:
        if a < b:
            tmp = a
            a = b
            b = tmp
        a = a % b
        if a == 0:
            return b
    return a


a = int(input("Podaj pierwszą liczbę do obliczenia największego wspólnego dzielnika: "))
b = int(input("Podaj drugą liczbę do obliczenia największego wspólnego dzielnika: "))

wynik = nwd(a, b)

print(
    "Największy wspólny dzielnik liczb: "
    + str(a)
    + " oraz "
    + str(b)
    + ", to: "
    + str(wynik)
    + "."
)
