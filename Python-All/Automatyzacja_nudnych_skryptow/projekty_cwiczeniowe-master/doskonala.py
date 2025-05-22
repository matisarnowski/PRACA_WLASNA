#!/usr/bin/python3

print(
    "Liczba doiskonała - liczba naturalna, która jest sumą wszystkich swych dzielników właściwych (to znaczy od niej mniejszych): "
)

global licz

licz = int(
    input("Podaj liczbę, która ma byyć sprawdzona pod tym kątem, czy jest doskonała. ")
)

lista = []

suma = 0
k = 0
for i in range(1, licz):
    if licz % i == 0:
        suma += i
        lista.append(i)
        k += 1

if suma == licz:
    print("Liczba ", licz, "jest liczbą doskonałą. ")
    print("Jej wszystkie dzielniki mniejsze od niej, to: ")
    for j in range(0, k):
        print(lista[j])
    print("Ich suma, to: ", suma)

elif suma < licz:
    print("Liczba ", licz, "jest liczbą niedoborową. ")
    print("Jej wszystkie dzielniki mniejsze od niej, to: ")
    for j in range(0, k):
        print(lista[j])
    print("Ich suma, to: ", suma)

else:
    print("Liczba ", licz, "jest liczbą nadmiarową. ")
    print("Jej wszystkie dzielniki mniejsze od niej, to: ")
    for j in range(0, k):
        print(lista[j])
    print("Ich suma, to: ", suma)
