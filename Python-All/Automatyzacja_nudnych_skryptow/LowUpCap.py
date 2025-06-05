#!/usr/bin/python3


def low_up_cap(tekst):
    print(
        """ If you want to change letters to lowercase, select: l.
    If you want to change to upper case, please select: u.
    If you want to change only the first letter of the string to uppercase, select: c."""
    )

    while True:
        wejscie = input("")

        if wejscie == "l":
            tekst = tekst.lower()
        elif wejscie == "u":
            tekst = tekst.upper()
        elif wejscie == "c":
            tekst = tekst.capitalize()
        else:
            print("End of operation!")
            break

    return tekst
