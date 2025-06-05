#!/usr/bin/python3.7

import pprint


def zliczanie(message):
    slownik = {}

    for znaki in message:
        slownik.setdefault(znaki, 0)
        slownik[znaki] = slownik[znaki] + 1

    return slownik


message = input("Podaj dowolnej długości tekst. ")

efekt = zliczanie(message)

pprint.pprint(efekt, width=1)
