class Text:
    def get_text(self):
        text = input(
            "Podaj treść, która zostanie następnie zaszyfrowana szyfrem Cezara. "
        )

        if len(text) > 0:
            return text
        else:
            print("Podaj choć jeden znak. Próbuj jeszcze raz.")
            self.get_text()
