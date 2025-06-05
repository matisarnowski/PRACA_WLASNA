def silnia(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return n * silnia(n - 1)


n = int(input("Podaj liczbę  do obliczenia silni: "))

print("Silnia z: " + str(n) + ", to: " + str(silnia(n)) + ".")
