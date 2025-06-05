import math
import pprint

if __name__ == "__main__":
    func = lambda x: x * x
    print(func(121))

    main_tab = []
    max_counting = 1
    prime_numbers = 0
    test = lambda x, y: True if x % y == 0 else False
    for i in range(2, 100):
        count = 1
        tab = []
        for j in range(2, i + 1):
            if test(i, j):
                if i != j:
                    phrase1 = str(j) + " jest dzielnikiem liczby: " + str(i)
                    tab.append(phrase1)
                count += 1
        if count == 2:
            phrase2 = str(j) + " Jest to liczba pierwsza. "
            prime_numbers += 1
        else:
            phrase2 = "Dzielnikow liczby: " + str(i) + " jest: " + str(count)
            if count > max_counting:
                max_counting_str = " Najwiecej dzielnikow ma liczba: " + str(j)
                max_counting = count
        tab.append(phrase2)
        main_tab.append(tab)

    with open("lista_liczb.txt", "w+") as file:
        for i in main_tab:
            for j in i:
                file.writelines(str(j) + "\n")
        file.writelines(max_counting_str + "\n")
        file.writelines("Liczb pierwszych jest: " + str(prime_numbers))
