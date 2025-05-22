#!/usr/bin/python3.7

lista = ["pierwszy", "drugi", "trzeci", "czwarty", "piąty"]


def pobieranie_tekstu(lista):
    print("`", end="")
    for i in range(0, len(lista)):
        if i < len(lista) - 1:
            print(lista[i] + ", ", end="")
        else:
            print(lista[i], end="")
    print("`")


pobieranie_tekstu(lista)

lista_1 = []

wyraz = ""
while wyraz != "koniec":
    wyraz = str(input("Podaj kolejną wartość na liście, i zakończ: 'koniec'"))
    if wyraz != "koniec":
        lista_1.append(wyraz)

if len(lista_1) == 0:
    print()
else:
    pobieranie_tekstu(lista_1)
