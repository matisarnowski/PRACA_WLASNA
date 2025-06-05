#!/usr/bin/python3
from Lotto import Lotto
from UrlLotto import UrlLotto
from Comparison import Comparison


def main():
    lotto = Lotto()
    list_lotto = []
    list_lotto = lotto.get_list_of_numbers()
    print("Wyniki przypadkowego losowania, to: ", str(list_lotto))
    url_lotto = UrlLotto()
    list_url_lotto = url_lotto.open_and_write_url()
    comparison = Comparison()
    the_end = comparison.get_comparison(
        url_lotto.how_much_lines(), list_lotto, list_url_lotto
    )
    print("Z porównania wychodzi: ", the_end)


if __name__ == "__main__":
    main()
