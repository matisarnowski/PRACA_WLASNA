#!/usr/bin/python3
import os

with open("Output.txt", "a+") as txt_file:
    str_to_file = input("Podaj słowo po angielsku do przetłumaczenia: ")
    str_to_file = "trans " + str_to_file + " >> Output.txt"
    tr = eval(str_to_file)
    os.system(tr)
