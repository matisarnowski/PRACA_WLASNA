from Key import Key
from Text import Text


class Encryption:
    def get_encryption(self):
        true_text = ""
        key = Key()
        key_valid = []
        key_valid = key.format_key()
        text = Text()
        text_valid = " "
        text_valid = text.get_text()
        i = 0
        for characters in text_valid:
            number = key_valid[i]
            if (
                (96 < ord(characters) and ord(characters) < 123)
                or (64 < ord(characters) and ord(characters) < 91)
            ) is False:
                true_text = true_text + " "
            if characters.isupper() and ord(characters) + number < 91:
                true_text = true_text + chr(ord(characters) + number)
            elif characters.isupper() and ord(characters) + number > 90:
                number = number % 26
                true_text = true_text + chr(64 + number)
            elif characters.islower() and ord(characters) + number < 123:
                true_text = true_text + chr(ord(characters) + number)
            elif characters.islower() and ord(characters) + number > 122:
                number = number % 26
                true_text = true_text + chr(96 + number)
            i += 1
            if i == len(key_valid):
                i = 0

        return true_text
