#!/usr/bin/python3


def encrypt(letter, number):
    encryption = (ord(letter) + number) % 256
    if encryption < 0:
        encryption += 256
    return encryption


# writing = input('Podaj tekst do zaszyfrowania: ')


def writing_encrypt(writing):
    encryption_table = []
    counter = 1
    for letter in writing:
        encryption_table.append(encrypt(letter, counter))
        counter += 1
    final_writing = ""
    for signs in encryption_table:
        final_writing += chr(signs)
    print(final_writing)
    return (
        final_writing
        + " liczba znaków, która została zaszysfrowana: "
        + str(counter - 1)
    )
