#!/usr/bin/python3

import LowUpCap, ObrobkaGraficznaTxt, otwieranieIwczytywanie

print(
    """Choose what you want to do!
Change all letters to lowercase uppercase! - 1
Align to either side! - 2
Exit - any key except 1, 2"""
)

tekst = otwieranieIwczytywanie.otwieranie_i_wczytywanie()

while True:
    print(
        """Choose what you want to do!
    Change all letters to lowercase uppercase! - 1
    Align to either side! - 2
    Exit - any key except 1, 2"""
    )

    wybor = input("")

    if wybor == "1":
        tekst = LowUpCap.low_up_cap(tekst)
    elif wybor == "2":
        tekst = ObrobkaGraficznaTxt.obrobka_graficzna_txt(tekst)
    else:
        print(tekst)
        break
