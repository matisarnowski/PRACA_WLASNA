#! python3
from randomQuizCountryGenerator import *


def play_total():
    total = 0
    my_set = random_quiz_country()
    print(my_set)
    for i, j, k in my_set:
        print(f"Dla kraju: {k}, stolicą jest: \n {i}.")
        capital = input("Podaj A, B, C lub D. Każda inna odpowiedź będzie błędna.")
        if capital == j:
            total += 1
    return total
