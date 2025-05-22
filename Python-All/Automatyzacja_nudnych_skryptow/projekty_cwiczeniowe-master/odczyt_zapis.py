plikzHaslem = open("haslo.txt", "r")

porownanie = plikzHaslem.read()
porownanie = porownanie.rstrip()

porownywane = input("Podaj hasło: ")

print(porownywane)
print(porownanie)
if porownanie == porownywane:
    plik = open("latarnik.txt", "r")

    zapis = plik.read()

    print(zapis)

    plik.close()
else:
    print("Brak dostępu. ")
