#!/usr/bin/python3.7

import math


def ciag(fib):
    if fib == 1:
        return 1
    elif fib == 2:
        return 1
    else:
        return ciag(fib - 1) + ciag(fib - 2)


x = 5


def jawny(fib_j):
    return (1 / math.sqrt(x)) * (
        ((1 + math.sqrt(x)) / 2) ** fib_j - ((1 - math.sqrt(x)) / 2) ** fib_j
    )


print("Podaj, który element ciągu Fibonnacciego chcesz wyliczyć: ")

fib = int(input())
fib_j = float(fib)
print(
    str(fib)
    + "-ty, element ciągu Fibonnacciego to według wzoru rekurencyjnego: "
    + str(ciag(fib))
)
print(
    str(fib)
    + "-ty, element ciągu Fibonnacciego to według wzoru jawnego: "
    + str(int(jawny(fib_j)))
)
