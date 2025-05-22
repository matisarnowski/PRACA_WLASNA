#!/usr/bin/python3


def gra(slowo, wygrana):
    blad = 0
    szubienica = [
        "",
        "________        ",
        "|               ",
        "|        |      ",
        "|        0      ",
        "|       /|\     ",
        "|       / \     ",
        "|               ",
    ]
    zasob_liter = list(slowo)
    pole = ["_"] * len(slowo)
    win = False
    print("Gra w wisielca!")
    while blad < len(szubienica) - 1:
        wiadomosc = "Odgadnij lietrę: "
        znak = input(wiadomosc)
        if znak in zasob_liter:
            odgadniete = zasob_liter.index(znak)
            pole[odgadniete] = znak
            zasob_liter[odgadniete] = "$"
        else:
            blad += 1
        print((" ".join(pole)))
        e = blad + 1
        print("\n".join(szubienica[0:e]))
        if "_" not in pole:
            print("Jesteś zwycięzcą! ")
            print(" ".join(pole))
            win = True
            wygrana += 1
            print("Masz {}, zwycięstw na koncie.".format(wygrana))
            return wygrana
    if not win:
        print("\n".join(szubienica[0:blad]))
        print("Przegrałeś! Miałeś odgadnąć: {}.".format(slowo))
        wygrana += 0
        return wygrana


moje_slowa = []
with open("gra_w_wisielce/EnglishVocabulary.txt", "r") as lista_slow:
    moje_slowa = lista_slow.read()

moje_slowa = moje_slowa.split("\n")

moje_slowa.pop()

slowka_angielskie = []
slowka_polskie = []

for i in range(len(moje_slowa)):
    if i % 2 == 0:
        slowka_angielskie.append(moje_slowa[i])
    else:
        slowka_polskie.append(moje_slowa[i])

# if len(slowka_angielskie) == len(slowka_polskie):
#    print('Prawda')
# else:
#    print('Fałsz')

wygrana = 0
for i in range(len(slowka_polskie)):
    print("Twoje słówko do dogadnięcia, to: \n{}".format(slowka_polskie[i]))
    slowo = slowka_angielskie[i]
    wygrana = gra(slowo, wygrana)

print("Koniec Gry!")
