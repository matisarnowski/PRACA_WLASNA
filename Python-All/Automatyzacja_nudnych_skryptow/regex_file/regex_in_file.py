#!/usr/bin/python3
import re
import os

path = os.path.join("/home/mateusz/Dokumenty/")
file_searching_pdf = re.compile(r"pdf?")
file_searching_jpg = re.compile(r"jpg?")
file_searching_txt = re.compile(r"txt?")

lista_pdf = []
lista_jpg = []
lista_txt = []
pdf = 0
for foldery, podfoldery, pliki in os.walk(path):
    for plik in pliki:
        if file_searching_pdf.search(plik):
            lista_pdf.append(os.path.join(path, foldery, plik))
            pdf += 1
for j in lista_pdf:
    print(j)
jpg = 0
for foldery, podfoldery, pliki in os.walk(path):
    for plik in pliki:
        if file_searching_jpg.search(plik):
            lista_jpg.append(os.path.join(path, foldery, plik))
            jpg += 1
for k in lista_jpg:
    print(k)
txt = 0
for foldery, podfoldery, pliki in os.walk(path):
    for plik in pliki:
        if file_searching_txt.search(plik):
            lista_txt.append(os.path.join(path, foldery, plik))
            txt += 1
for l in lista_txt:
    print(l)
print("Znaleziono: %d plików z rozszezrzeniem pdf." % pdf)
print("Znaleziono: %d plików z rozszezrzeniem jpg." % jpg)
print("Znaleziono: %d plików z rozszezrzeniem txt." % txt)
