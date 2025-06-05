#!/usr/bin/python3

from boxPrint import *
import sys

if __name__ == "__main__":
    print(sys.argv)
    try:
        width = int(sys.argv[2])
        heigth = int(sys.argv[3])
    except ValueError as err:
        print(err + "Podaj liczbę całkowitą jako wysokość i szerokość")

    try:
        if len(sys.argv) == 4:
            try:
                boxPrint(sys.argv[1], width, heigth)
            except Exception as err:
                print(f"Nastąpiło zgłoszenie wyjątku: {str(err)}")
    except Exception as err:
        print(err)
