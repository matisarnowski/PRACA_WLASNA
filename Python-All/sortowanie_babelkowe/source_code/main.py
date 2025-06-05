from function_bubble_sort import *
from function_random_numbers import *
from plot_of_numbers import *
import pprint

if __name__ == "__main__":
    while True:
        try:
            n = input(
                "Wprowadż liczbę naturalną, mówiącą ile losowych liczb chcesz wygenerować, będą to liczby naturalne od 0 do 100. Aby je następnie posortować: "
            )
            n = int(n)
            if n < 2:
                print("Wprowadź liczbę naturalną większą od dwóch.")
                continue
        except Exception as e:
            print(e)
            continue
        break
    tab = random_numbers(n)
    finished_sorting = bubble_sort(tab)
    pprint.pprint(finished_sorting)
    plot_list(finished_sorting)
