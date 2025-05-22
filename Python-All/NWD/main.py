def func_nwd(a, b):
    nwd = 1
    list_a = list(filter(lambda n: a % n == 0, range(2, round(a + 1))))
    list_b = list(filter(lambda m: b % m == 0, range(2, round(b + 1))))
    for x in list_a:
        if x in list_b:
            nwd = x
    return nwd


if __name__ == "__main__":
    a = int(
        input("Podaj pierwszą liczbę, do obliczenia największego wspólnego dzielnika: ")
    )
    b = int(input("Podaj drugą liczbę. "))
    print(func_nwd(a, b))
