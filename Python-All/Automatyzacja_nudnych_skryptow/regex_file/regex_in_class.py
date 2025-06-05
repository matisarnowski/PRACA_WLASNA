import re
import os


class regex_in_class:
    PATH = os.path.join("/home/mateusz/Dokumenty")

    def __init__(self, STRING):
        self.STRING = STRING
        self.file_searching = self.extend_of_file()
        self.list_path = []

    def extend_of_file(self):
        if self.STRING == "pdf" or "txt" or "jpg":
            return re.compile(self.STRING + "?")
        else:
            return self.STRING

    def print_list_method(self):
        i = 0
        for foldery, podfoldery, pliki in os.walk(self.PATH):
            for plik in pliki:
                if self.file_searching.search(plik):
                    self.list_path.append(os.path.join(self.PATH, foldery, plik))
                    i += 1
        for j in self.list_path:
            print(j)
        print("Znaleziono: %d plików z rozszezrzeniem %s." % (i, self.STRING))
