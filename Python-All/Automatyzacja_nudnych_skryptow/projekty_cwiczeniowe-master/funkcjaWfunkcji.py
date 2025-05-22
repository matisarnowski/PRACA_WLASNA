#!/usr/bin/python3


def dane():
    imie = input("Podaj swoje imię: \n")
    nazwisko = input("Podaj swoje nazwisko: \n")
    PESEL = input("Podaj swój numer PESEL: \n")
    data_urodzenia = input("Podaj swoją datę urodzenia: \n")
    miejscowosc = input("Podaj miejscowosc, w której mieszkaszś: \n")
    kod_pocztowy = input("Podaj kod pocztowy, który ma twoja miejscowość: \n")
    znaki = (
        imie
        + " "
        + nazwisko
        + " "
        + PESEL
        + " "
        + data_urodzenia
        + " "
        + miejscowosc
        + " "
        + kod_pocztowy
    )
    return znaki


def drukowanie(znaki):
    print(znaki)


drukowanie(dane())
