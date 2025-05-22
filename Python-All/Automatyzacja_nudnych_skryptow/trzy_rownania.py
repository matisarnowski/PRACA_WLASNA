#!/usr/bin/python3


def wyznacznik(x_1, x_2, x_3, y_1, y_2, y_3, z_1, z_2, z_3):
    return (
        x_1 * y_2 * z_3
        + y_1 * z_2 * x_3
        + z_1 * x_2 * y_3
        - z_3 * y_2 * x_1
        - y_3 * z_2 * x_1
        - z_3 * x_2 * y_1
    )


print("Program liczy niewiadome układu trzech równań, metodą Cramera, wyznaczników. ")

a_1 = float(input("Wprowadź pierwszy współczynnik z pierwszego równania: "))
a_2 = float(input("Wprowadź drugi współczynnik z pierwszego równania: "))
a_3 = float(input("Wprowadź trzeci współczynnik z pierwszego równania: "))

b_1 = float(input("Wprowadź pierwszy współczynnik z drugiego równania: "))
b_2 = float(input("Wprowadź drugi współczynnik z drugiego równania: "))
b_3 = float(input("Wprowadź trzeci współczynnik z drugiego równania: "))

c_1 = float(input("Wprowadź pierwszy współczynnik z trzeciego równania: "))
c_2 = float(input("Wprowadź drugi współczynnik z trzeciego równania: "))
c_3 = float(input("Wprowadź pierwszy współczynnik z trzeciego równania: "))

d_1 = float(input("Wprowadź wyraz wolny z pierwszego równania: "))
d_2 = float(input("Wprowadź wyraz wolny z drugiego równania: "))
d_3 = float(input("Wprowadź wyraz wolny z trzeciego równania: "))

wyznacznik_macierzy = wyznacznik(a_1, a_2, a_3, b_1, b_2, b_3, c_1, c_2, c_3)

wyznacznik_x = wyznacznik(d_1, d_2, d_3, b_1, b_2, b_3, c_1, c_2, c_3)

wyznacznik_y = wyznacznik(a_1, a_2, a_3, d_1, d_2, d_3, c_1, c_2, c_3)

wyznacznik_z = wyznacznik(a_1, a_2, a_3, b_1, b_2, b_3, d_1, d_2, d_3)

if wyznacznik_macierzy == 0 and (
    wyznacznik_x == 0 and wyznacznik_y == 0 and wyznacznik_z == 0
):
    print("Układ równań ma nieskończenie wiele rozwiązań. ")
elif wyznacznik_macierzy == 0 and (
    (wyznacznik_x != 0 or wyznacznik_y != 0 or wyznacznik_z != 0)
):
    print("Układ równań jest sprzeczny, nie ma rozwiązań w liczbach rzeczywistych. ")
else:
    x = wyznacznik_x / wyznacznik_macierzy
    y = wyznacznik_y / wyznacznik_macierzy
    z = wyznacznik_z / wyznacznik_macierzy
    print(
        "Dla zadanego układu równań, rozwiązaniem jest trójka liczb: ",
        x,
        "; ",
        y,
        "; ",
        z,
        "!",
    )
