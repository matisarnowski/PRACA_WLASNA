def bubble_sort(tab):
    n = len(tab)
    switched_places = True
    while switched_places:
        switched_places = False
        last_index = 0
        for i in range(1, n):
            if tab[i - 1] > tab[i]:
                tab[i - 1], tab[i] = tab[i], tab[i - 1]
                switched_places = True
                last_index = i
        n = last_index
    return tab
