#!/usr/bin/python3


def boxPrint(symbol, width, height):
    """ "
    Rysuje prostokąt z podanego znaku. Przy wyznaczonej szerokości i wysokości. Podaj jako pierwszy argument znak, który ma być narysowany.
    Jako drugi argument szerokość prostokąta, jako trzeci jego wysokość.
    """

    if len(symbol) != 1:
        raise Exception("Symbol musi być znakiem.")
    if width <= 2:
        raise Exception("Szerokość musi mieć większą wartość niż 2.")
    if height <= 2:
        raise Exception("Wysokość musi mieć większą wartość niż 2.")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)
