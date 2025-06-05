import random

my_numbers = []

for i in range(100):
    my_numbers.append(random.randint(1, 1001))


def quick_sort(tabel_with_numbers):
    if len(tabel_with_numbers) <= 1:
        return tabel_with_numbers
    pivot = tabel_with_numbers.pop()
    left = [number for number in tabel_with_numbers if number <= pivot]
    right = [number for number in tabel_with_numbers if number > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


my_numbers = quick_sort(my_numbers)

print(my_numbers)
