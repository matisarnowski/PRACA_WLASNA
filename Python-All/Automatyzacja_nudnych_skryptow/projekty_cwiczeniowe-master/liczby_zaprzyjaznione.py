def dzielniki(licz):
    suma = 0
    for i in range(1, licz):
        if licz % i == 0:
            suma += i
    return suma


print(
    "Liczby zaprzyjaźnione to para liczb naturalnych, takich, że suma dzielników właściwych każdej z tych liczb równa się drugiej. Dzielniki właściwe są to wszystkie dzielniki danej liczby oprócz niej samej. "
)

licz_a = int(input("Podaj pierwszą liczbę do testu: "))
licz_b = int(input("Podaj drugą liczbę do testu: "))

if dzielniki(licz_a) == licz_b and dzielniki(licz_b) == licz_a:
    print(
        "Liczby "
        + str(licz_a)
        + " oraz "
        + str(licz_b)
        + ", to liczby zaprzyjaźnione. "
    )
    print(
        "Suma dzielnków właściwych, liczby "
        + str(licz_a)
        + ", to: "
        + str(dzielniki(licz_a))
        + ", a liczby: "
        + str(licz_b)
        + ", to: "
        + str(dzielniki(licz_b))
        + "."
    )
else:
    print(
        "Niestety liczby "
        + str(licz_a)
        + " oraz "
        + str(licz_b)
        + ", nie są liczbami zaprzyjaźnionymi. "
    )
    print(
        "Suma dzielnków właściwych, liczby "
        + str(licz_a)
        + ", to: "
        + str(dzielniki(licz_a))
        + ", a liczby: "
        + str(licz_b)
        + ", to: "
        + str(dzielniki(licz_b))
        + "."
    )
