""" 
Zadanie. 1
Dana jest lista 
Kolo = [-3,7,2,0,5,1,-2]
Napisz program, który na podstawie listy Kolo wydrukuje następującą 'grafikę':
-3 [1]
[2] 7
[3] 2
[4] 0
[5] 5
[6] 1
-2 [7]
"""
Kolo = [-3, 7, 2, 0, 5, 1, -2]

j = 1
for i in Kolo:
    if j == 1 or j == len(Kolo):
        print(str(i) + " [" + str(j) + "]")
    else:
        print("[" + str(j) + "] " + str(i))
    j += 1

"""
Zadanie 2.
Poniższy program generuje tablicę, której elementami są 
losowe liczby z przedziału od 1 do 5.
from random import randint
tablica = []
for i in range(100):
    tablica.append(randint(1,5))

Uzupełnij kod programu, aby uzyskać następujący efekt:
-program zlicza i podaje ilość wystąpień liczby 2
"""
from random import randint

tablica = []
for i in range(100):
    tablica.append(randint(1, 5))
total_2 = 0
total_tab_2 = 0
for j in tablica:
    if j == 2:
        total_2 += 1
        total_tab_2 += j

print("Wystąpień liczby 2:", total_2, "Suma wystąpień liczby 2:", total_tab_2)

"""
Zadanie 3.
Dla podanej niezerowej liczby całkowitej n zbadać, czy jest 
ona dodatnia. Jeżeli jest dodatnia, sprawdzić jej 
podzielność przez 5. Jeżeli jest ujemna , sprawdzić jej 
podzielność przez 3. Wynikiem działania programu ma być 
dokładnie taki komunikat:
Liczba n jest [dodatnia|ujemna] i [jest|nie jest]
podzielna przez [5|3]
Przykład. Dla n=6 wynikiem działania programu będzie
komunikat:
Liczba 6 jest dodatnia i nie jest podzielna przez 5.
Uwaga. Przykładowe, niepoprawne rozwiązanie:
Liczba 6 jest dodatnia.
Liczba 6 jest nie podzielna przez 5. 
"""
number = int(input("Podaj liczbę całkowitą:"))
dodatnia = "dodatnia"
ujemna = "ujemna"
jest = "jest"
nie_jest = "nie jest"
five = "5"
three = "3"
a = ""
b = ""
c = ""
if number > 0:
    if number % 5 == 0:
        a = dodatnia
        b = jest
        c = five
    else:
        a = dodatnia
        b = nie_jest
        c = five
elif number < 0:
    if number % 3 == 0:
        a = ujemna
        b = jest
        c = three
    else:
        a = ujemna
        b = nie_jest
        c = three
print(
    "Liczba " + str(number) + " jest " + a + " i " + b + " podzielna przez " + c + "."
)

"""
Zadanie 4.
Dal podanych liczb naturalnych m, k, oznaczających masę 
ciała (kg) i ilość przebięgniętych kilometrów, wyliczyć 
liczbę spalonych kalorii według wzoru m*k. Wypisać na 
ekranie: masę ciała, ilość przebiegniętych kilometrów oraz 
ilość spalonych kalorii, a w przypadku przekroczenia
progu kcal=1500 program ma dodatkowo wypisać na ekranie
komunikat "Uwaga - pamiętaj o nawodnienu organizmu". 
"""
masa = input("Podaj masę ciała w kg: ")
kilometry = input("Podaj ilosć przebiegniętych kilometrów: ")
kcal = float(masa) * float(kilometry)
prog = ""
if kcal >= 1500:
    prog = "Uwaga - pamiętaj o nawodnieniu organizmu"
print(
    "Masa ciała {}, ilość przebiegniętych kilomterów {}, ilość spalonych kalorii {}.\n{}".format(
        masa, kilometry, kcal, prog
    )
)

"""
Zadanie 5. (numer albumu parzysty)
Dal podanej liczby naturalnej n wyrysować figurę,
składającą się z wypełnionego kwadratu n xn. Zakładamy,
że n > 2.
Przykład. Wynik działania programu dla n=4
xxxx
xoox
xoox
xxxx    
"""
number = int(input("Podaj liczbę > 2: "))
for i in range(0, number):
    if not (i == 0 or i == number - 1):
        print("x" + (number - 2) * "o" + "x")
    else:
        print(number * "x")
