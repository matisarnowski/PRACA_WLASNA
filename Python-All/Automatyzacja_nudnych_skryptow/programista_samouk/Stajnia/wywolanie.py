#!/usr/bin/python3


class Rider:
    def __init__(self, n, a):
        self.name = n
        self.age = a


class Horse:
    def __init__(self, n, a, o):
        self.name = n
        self.age = a
        self.owner = o


rider_ela = Rider("Elżbieta", 52)
horse_mateusz = Horse("Mateusz", 32, rider_ela)

print(
    "Koń: "
    + horse_mateusz.name
    + ", ma właściciela: "
    + horse_mateusz.owner.name
    + ", w wieku: "
    + str(horse_mateusz.owner.age)
)
