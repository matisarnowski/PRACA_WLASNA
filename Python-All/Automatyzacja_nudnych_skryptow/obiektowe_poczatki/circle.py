#!/usr/bin/python3


class Circle:
    from math import pi as p

    def __init__(self, promien, ludolfina=p):
        self.promien = promien
        self.ludolfina = ludolfina

    def pole(self):
        return self.promien * self.ludolfina

    def obwod(self):
        return 2 * self.promien * self.ludolfina
