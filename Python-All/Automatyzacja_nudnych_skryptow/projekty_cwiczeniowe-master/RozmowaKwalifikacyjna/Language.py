import json
import os
from pathlib import Path


class Language:
    path = "/home/mateusz/Dokumenty/Dokumenty/informatyka/Python/python_code/projekty_cwiczeniowe-master/RozmowaKwalifikacyjna/dictLanguage.json"

    def __init__(self):
        self.language_dict = self.read_dict_language()

    def set_language_name(self):
        while True:
            language_name = input(
                "Podaj nazwę języka programowania, co do którego przeglądasz ofertę pracy: "
            )
            language_name = language_name.lower()
            if len(language_name) != 0:
                if language_name in self.language_dict.keys():
                    self.language_dict[language_name] += 1
                else:
                    self.language_dict[language_name] = 1
                return language_name
            print("Nazwa języka nie może być pusta. \n")

    def read_dict_language(self):
        with open(self.path) as file:
            if Path(self.path).stat().st_size == 0:
                return dict()
            return json.loads(file.read())

    def write_dict_language(self):
        with open(self.path, "w") as file:
            file.write(json.dumps(self.language_dict))
            return self.language_dict
