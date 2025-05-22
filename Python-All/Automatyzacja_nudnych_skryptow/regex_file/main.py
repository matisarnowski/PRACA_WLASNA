#!/usr/bin/python3
from automatyzacja.regex_file.regex_in_class import *


if __name__ == "__main__":
    STRING = input("Podaj rozszezrzenie, które chcesz znaleźć: ")
    regex = regex_in_class(STRING)
    regex.print_list_method()
