#!/usr/bin/python3


class Triangle:
    from math import sqrt as p

    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc

    def pole(self):
        return (self.podstawa * self.wysokosc) / 2

    def obwod(self):
        return (
            self.podstawa
            + self.wysokosc
            + self.p(self.podstawa**2 + self.wysokosc**2)
        )
