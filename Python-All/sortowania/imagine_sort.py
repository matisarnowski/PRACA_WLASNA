import random

my_numbers = [random.randint(0, 1001) for _ in range(100)]


def imagine_sort(my_numbers):
    i = 0
    tab = []
    length = len(my_numbers)
    while i < length:
        minimum = my_numbers[i]
        j = i + 1
        while j < length:
            if my_numbers[j] <= minimum:
                minimum = my_numbers[j]
            j += 1
        tab.append(minimum)
        my_numbers.remove(minimum)
        length -= 1
        i += 1
    return tab


print(imagine_sort(my_numbers))
