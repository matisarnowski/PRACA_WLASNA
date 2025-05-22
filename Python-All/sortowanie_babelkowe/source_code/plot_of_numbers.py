import numpy as np
import matplotlib.pyplot as plt


def plot_list(tab):
    data = np.array(tab)
    x = np.arange(len(data))
    plt.plot(x, data)
    plt.xlabel("Indeks")
    plt.ylabel("Liczba")
    plt.title("Wykres liczby z tablicy")
    plt.show()
