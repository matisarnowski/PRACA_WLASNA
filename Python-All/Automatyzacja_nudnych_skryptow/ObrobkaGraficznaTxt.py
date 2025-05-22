#!/usr/bin/python3


def obrobka_graficzna_txt(tekst):
    print(
        """If you want to align left choose: l.
    If you want to align to the right choose: r.
    If you want to center, select: c."""
    )

    tekst_lista = tekst.split("\n")
    tekst = ""

    while True:
        wybor = input("")

        if wybor == "l":
            for i in tekst_lista:
                tekst = tekst + i.ljust(88, "^") + "\n"
        elif wybor == "r":
            for i in tekst_lista:
                tekst = tekst + i.rjust(88, "^") + "\n"
        elif wybor == "c":
            for i in tekst_lista:
                tekst = tekst + i.center(88, "^") + "\n"
        else:
            print("End of operation")
            break

    return tekst
