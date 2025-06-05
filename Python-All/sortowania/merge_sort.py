import random

my_numbers = []

for i in range(100):
    my_numbers.append(random.randint(1, 1001))
center_of_merge = 0


def merge(tab, start, center, end):
    temp_tab = [x for x in range(end - start)]
    i = start
    j = center + 1
    k = 0

    while i <= center and j <= end:
        if tab[i] <= tab[j]:
            temp_tab[k] = tab[i]
            i += 1
        else:
            temp_tab[k] = tab[j]
            j += 1
        k += 1

    while i <= center:
        temp_tab[k] = tab[i]
        i += 1
        k += 1

    while j <= end:
        temp_tab[k] = tab[j]
        j += 1
        k += 1

    for l in range(0, (end - start)):
        tab[start + l] = temp_tab[l]


def merge_sort(tab, start, end):
    if start != end:
        center_of_merge = (end + start) // 2

        merge_sort(tab, start, center_of_merge)
        merge_sort(tab, center_of_merge + 1, end)

        merge(tab, start, center_of_merge, end)


merge_sort(my_numbers, 0, len(my_numbers) - 1)

print(my_numbers)
