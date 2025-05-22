#! /usr/bin/python3
# mcb.pyw - Zapisuje i wczytuje do schowka fragmenty tekstu.
# Użycie: py.exe mcb.pyw save <słowo-kluczowe> - Wczytanie słowa kluczowego do schowka.
# py.exe mcb.pyw list - Wczytywanie wszsytkich słów kluczowych do schowka.

import shelve, pyperclip,sys

mcbShelf = shelve.open('mcb')

#TODO: Zapis zawartości schowka.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'paste':
    print(mcbShelf[sys.argv[2]])
elif len(sys.argv) == 2:
    #TODO: Wyświetlanie listy słów kluczowych i wczytywanie treści.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
