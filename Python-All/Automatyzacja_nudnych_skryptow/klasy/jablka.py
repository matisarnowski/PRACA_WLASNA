#!/usr/bin/python3


class Apple:
    def __init__(self, n, w, k, d):
        """Waga jest podana w gramach. Wiek w dniach. Temparatura przechowywania, to średnia temparatura w ciągu dnia."""

        self.nazwa = n
        self.waga = w
        self.kolor = k
        self.dni = d
        print(
            "Nazwa: ", n, " Masa: ", w, " w gramach. Kolor: ", k, " Wiek w dniach: ", d
        )


lobo = Apple("Lobo", 250, "żółte", 200)
jonagold = Apple("Jonagold", 300, "czerwone", 60)
