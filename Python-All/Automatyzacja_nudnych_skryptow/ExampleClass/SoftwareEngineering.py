#!/usr/bin/python3


class SoftwareEngineering:
    # class attributes
    allias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writting code...")

    def code_in_language(self, language):
        print(f"{self.name} is witting code in {language}")

    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}PLN"
        return information

    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}PLN"
        return information

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.age == other.age
            and self.level == other.level
            and self.salary == other.salary
        )

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# instance
se1 = SoftwareEngineering("Mateusz", 33, "Junior", 5000)
se2 = SoftwareEngineering("Kuba", 29, "Senior", 7000)
se3 = SoftwareEngineering("Kuba", 29, "Senior", 7000)

print("%s  lubi %s" % (se1.name, se2.name))
se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("Java")
print(se1.information())
print(se2.information())
print(se1)
print(se2)
print(se2 == se3)
print(se2 is se3)
print(SoftwareEngineering.entry_salary(27))
