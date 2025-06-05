from math import sqrt

licz = int(
    input("Podaj liczbę naturalną. Zostanie sprawdzone, czy jest ona liczbą pierwszą: ")
)


dzielniki = 0

pier = sqrt(licz)

pier = int(pier)

for i in range(2, pier + 1):
    if licz % i == 0:
        dzielniki += 1
    else:
        dzielniki += 0

if licz == 1:
    print(
        "Jedynka nie jest, ani liczbą pierwszą, ani złożoną. Jest elementem neutralnym mnożenia. "
    )
else:
    if dzielniki < 1:
        print("Liczba ", licz, " jest liczbą pierwszą. ")
    else:
        print("Liczba ", licz, " jest liczbą złożoną. ")
