import json
from Language import Language
from pathlib import Path


class Requirement:
    path = "/home/mateusz/Dokumenty/Dokumenty/informatyka/Python/python_code/projekty_cwiczeniowe-master/RozmowaKwalifikacyjna/dictRequirement.json"

    def __init__(self, language_dict):
        self.language_dict = language_dict
        self.dict_requirement = self.read_requirement_dict()

    def set_requirement_name(self, language_name):
        print("Podaj nazwę wymagania dla języka programowania: ", language_name)
        requirement_name = input()
        requirement_name = requirement_name.lower()
        self.set_dict_requirement(language_name, requirement_name)

    def read_requirement_dict(self):
        with open(self.path) as file:
            if Path(self.path).stat().st_size == 0:
                return dict()
            return json.loads(file.read())

    def set_dict_requirement(self, language_name, requirement_name):
        while True:
            if len(requirement_name) != 0:
                if language_name not in self.dict_requirement.keys():
                    self.dict_requirement[language_name] = dict()
                if requirement_name in self.dict_requirement[language_name].keys():
                    self.dict_requirement[language_name][requirement_name] += 1
                else:
                    self.dict_requirement[language_name][requirement_name] = 1
                return self.dict_requirement
            print("Nazwa wymagania nie może być pusta")

    def write_requirements_name(self):
        with open(self.path, "w") as file:
            file.write(json.dumps(self.dict_requirement))
