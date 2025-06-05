class Key:
    def get_key(self):
        key_str = input(
            "Podaj klucz, którym chcesz zaszyfrować tekst. Niech to będzie jakieś dowolne słowo: "
        )

        if len(key_str) != 0:
            return key_str
        else:
            print("Wymagana długość, przynajmniej jeden znak.")
            self.get_key()

    def format_key(self):
        # print("Flaga1")
        key = ""
        key = self.get_key()
        # print(key)
        length_key = 0
        length_key = len(key)
        # print(length_key)
        true_key = []

        i = 0
        while i < length_key:
            true_key.append(ord(key[i]))
            i += 1

        return true_key
