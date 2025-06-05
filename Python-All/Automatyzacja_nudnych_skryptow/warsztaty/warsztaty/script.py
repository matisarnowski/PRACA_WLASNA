#!/usr/bin/python3

import csv
import numpy
import os


def is_equal(a, b):
    if a == b:
        return True


with open(
    os.path.join(os.getcwd(), "srednie_wyniki_egzaminu_maturalnego.csv")
) as csvfile:
    results = []
    readCSV = csv.reader(csvfile, delimiter=";")

    for row in readCSV:
        results.append(float(row[7].replace(",", ".")))

    mediana = numpy.median(results)

    print("Srodkowy wynik dla średnich wyników maturalnych to: ", mediana, "%.")

with open(
    os.path.join(os.getcwd(), "srednie_wyniki_egzaminu_maturalnego.csv")
) as csvfile:
    readCSV1 = csv.reader(csvfile, delimiter=";")

    for row1 in readCSV1:
        if float(row1[7].replace(",", ".")) == float(mediana):
            print(float(row1[7].replace(",", ".")))
            scores = []
            scores.append(row1[5])
            scores.append(row1[3])
            scores.append(row1[2])
            print(
                "W roku: ",
                scores[0],
                ", z przedmiotu: ",
                scores[1],
                ", poziom: ",
                scores[2],
            )
    print(max(results))
