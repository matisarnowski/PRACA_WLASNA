#!/usr/bin/python3
# change_date_format.py - Zmienia nazwę pliku wraz z datą w formacie amerykańskim (MM-DD-RRRR)
# na datę w formacie europesjskim (DD-MM-RRRR)

import shutil
import os
import re

# Utworzenie wyrażenia regularnego dopasowującego pliki zawierające w nazwie datę w formacie amerykańskim.

datePattern = re.compile(
    r"""^(.*?) # cały tekst przed datą
    ((0|1)?\d)- # jedna lub dwie cyfry określające miesiąc
    ((0|1|2|3)?\d)- # jedna lub dwie cyfry określające dzień
    ((19|20)\d\d) # cztery cyfry określające rok
    (.*?)$ # cały tekst po dacie
""",
    re.VERBOSE,
)

# TODO: Iteracja przez pliki znajdujące się w katalogu roboczym

for amerFilename in os.listdir("."):
    mo = datePattern.search(amerFilename)
    # TODO: Pominięcie plików bez daty

    if mo == None:
        continue
    # TODO: Pobranie poszczególnych fragmentów nazwy pliku

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # TODO: Przygotowanie nazwy pliku zawierającej datę w formacie europejskim
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

    # TODO: Pobranie pełnych bezwzględnych ścieżek dostępu do pliku
    absWorkingDir = os.path.abspath(".")
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # TODO: Zmiana nazwy plików
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename, euroFilename)
