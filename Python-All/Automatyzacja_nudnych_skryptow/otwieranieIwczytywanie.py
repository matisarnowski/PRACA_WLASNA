#!/usr/bin/python3


def otwieranie_i_wczytywanie():
    with open("\tekst.txt", "r") as plik:
        tekst = plik.read()
        return tekst


print(otwieranie_i_wczytywanie())
