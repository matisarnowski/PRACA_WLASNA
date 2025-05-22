while True:
    try:
        n = int(input("Podaj liczbę większą od 1. Liczbę naturalną: "))
    except:
        print(Exception("Podałeś niewłaściwą wartość. "))
        continue
    if n > 1:
        break
for i in range(0, n):
    print(" " + n * "*")
k = n + 2
for i in range(0, k):
    print(i * " " + (k - 2 * i) * "*")
