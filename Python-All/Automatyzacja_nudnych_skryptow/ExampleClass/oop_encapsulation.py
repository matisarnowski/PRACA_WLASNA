#!/usr/bin/python3


class SoftwareEngineer:
    pass

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._number_of_bug_solved = 0

    def code(self):
        self._number_of_bug_solved += 1

    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        self._salary = self._calculate_salary(value)

    def _calculate_salary(self, base_value):
        if self._number_of_bug_solved < 10:
            return base_value
        if self._number_of_bug_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer("Mateusz", 33)
for i in range(70):
    se.code()
se.set_salary(6000)
print(se.get_salary())
