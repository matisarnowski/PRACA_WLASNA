from math import sqrt

print(
    "Liczba jest super-pierwsza, gdy jest liczbą pierwszą i suma jej cyfr też jest liczbą pierwszą."
)
licz = int(
    input("Podaj liczbę, która ma zostać sprawdzona, czy jest liczbą super-pierwszą: ")
)

dzielniki = 0

pier = sqrt(licz)

pier = int(pier)

for i in range(2, pier + 1):
    if licz % i == 0:
        dzielniki += 1
    else:
        dzielniki += 0

super = licz
suma_super = 0

while super > 0:
    suma_super += super % 10
    super = (super - super % 10) / 10
    super = int(super)

dzielniki1 = 0

pier1 = sqrt(suma_super)

pier1 = int(pier1)

for i in range(2, pier1 + 1):
    if suma_super % i == 0:
        dzielniki1 += 1
    else:
        dzielniki1 += 0

if licz == 1:
    print(
        "Jedynka nie jest, ani liczbą pierwszą, ani złożoną. Jest elementem neutralnym mnożenia. "
    )
else:
    if dzielniki < 2 and dzielniki1 < 1:
        print("Liczba ", licz, " jest liczbą super-pierwszą. ")
    elif dzielniki < 2 and dzielniki1 >= 1:
        print("Liczba ", licz, " jest liczbą pierwszą, ale nie super-pierwszą. ")
    else:
        print("Liczba ", licz, " jest liczbą złożoną. ")
