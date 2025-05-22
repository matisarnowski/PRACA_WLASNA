#!/usr/bin/python3

import os

lokalizacja = "/home/mateusz/Dokumenty"
calosc = 0


def spr(lokalizacja):
    calosc = 0
    for path, dirs, files in os.walk(lokalizacja):
        for item in files:
            plik = os.path.join(path, item)
            calosc += os.path.getsize(plik)

    return calosc


def rysuj_procent(procent):
    for i in range(0, procent):
        print("%", end="")
    print(procent)


def oblicz_procent(calosc, ogolem):
    return int(round(calosc / ogolem * 100, 0))


lokalizacja_docs = "/home/mateusz/Dokumenty"
calosc_docs = spr(lokalizacja_docs)

lokalizacja_music = "/home/mateusz/Muzyka"
calosc_music = spr(lokalizacja_music)

lokalizacja_download = "/home/mateusz/Pobrane"
calosc_download = spr(lokalizacja_download)

lokalizacja_pictures = "/home/mateusz/Obrazy"
calosc_pictures = spr(lokalizacja_pictures)

ogolem = calosc_docs + calosc_music + calosc_download + calosc_pictures

procent_docs = oblicz_procent(calosc_docs, ogolem)
procent_music = oblicz_procent(calosc_music, ogolem)
procent_download = oblicz_procent(calosc_download, ogolem)
procent_pictures = oblicz_procent(calosc_pictures, ogolem)

print(
    "Ogółem foldery Dokumenty, Muzyka, Obrazy i Pobrane zajmują na moim Linuksowym dysku: ",
    round(ogolem / 1024**2, 2),
    " MiB. ",
)
print("Procentowo, folder Dokumenty spośród czterech wymienionych: ")
rysuj_procent(procent_docs)
print("Rzeczywisty rozmiar: ", round(calosc_docs / 1024**2, 2), " MiB.")

print("Procentowo, folder Muzyka spośród czterech wymienionych: ")
rysuj_procent(procent_music)
print("Rzeczywisty rozmiar: ", round(calosc_music / 1024**2, 2), " MiB.")

print("Procentowo, folder Pobrane spośród czterech wymienionych: ")
rysuj_procent(procent_download)
print("Rzeczywisty rozmiar: ", round(calosc_download / 1024**2, 2), " MiB.")

print("Procentowo, folder Obrazy spośród czterech wymienionych: ")
rysuj_procent(procent_pictures)
print("Rzeczywisty rozmiar: ", round(calosc_pictures / 1024**2, 2), " MiB.")
