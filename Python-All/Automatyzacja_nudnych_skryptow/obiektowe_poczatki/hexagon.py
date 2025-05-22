#!/usr/bin/python3


class Hexagon:
    from math import sqrt as p

    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return ((self.bok**2) * 6 * self.p(3)) / 4

    def obwod(self):
        return 6 * self.bok
