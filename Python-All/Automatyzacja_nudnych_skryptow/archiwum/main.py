#!/usr/bin/python3

import zipfile
import os


def backupToZip(folder):
    # Umieszczenie w archiwum ZIP całej zawartości katalogu

    folder = os.path.abspath(
        folder
    )  # Upewniamy się, że otrzymaliśmy bezwzględną ścieżkę dostępu do katalogu

    # Ustalenie nazwy pliku jaka powinna zostać użyta przez kod na podstawie istniejących plików

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number += 1

    # TODO: Utworzenie archiwum ZIP.
    print(f"Tworzenie archiwum {zipFilename}")
    backupZip = zipfile.ZipFile(zipFilename, "w")

    # Przejście przez całe drezwo katalogu i komptresjaplików we wszystkich podkatalogach
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Dodawanie plików w {foldername}")
        # Dodawanie bieżącego katalogu do archiwum ZIP
        backupZip.write(foldername)
        # Dodawanie wszystkich plików zanjdujących się w tym katalogu do archiwum ZIP

        for filename in filenames:
            newBase = os.path.basename(filename) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue  # w archiwum nie umieszczamy plików innych archiwów
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()


if __name__ == "__main__":
    backupToZip("example")
