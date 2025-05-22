import Lotto
import UrlLotto


class Comparison:
    def get_comparison(self, how_much_lines, list_lotto, list_url_lotto):
        bool_lotto = []
        i = 0
        while i < how_much_lines:
            for j in range(6):
                if list_url_lotto[i][j] == list_lotto[j]:
                    bool_lotto.append(True)
                else:
                    bool_lotto.append(False)
            k = 0
            while k < 6:
                if bool_lotto[k] is True:
                    for l in list_url_lotto:
                        list_url = []
                        list_url.append(l)
                    return "Lista z choć jednym trafionym numerem, to: " + str(list_url)
                else:
                    return "Brak trafień."
                k += 1

            i += 1
