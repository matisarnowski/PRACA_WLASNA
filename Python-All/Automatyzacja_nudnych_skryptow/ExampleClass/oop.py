#!/usr/bin/python3


# inherits, override, extend
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working... ")


class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.salary = salary

    def debug(self):
        print(f"{self.name} is debugging... ")

    def work(self):
        print(f"{self.name} is coding... ")


class Designer(Employee):
    pass

    def draw(self):
        print(f"{self.name} is drawing... ")

    def work(self):
        print(f"{self.name} is designing... ")


se = SoftwareEngineer("Mateusz", 33, 2500, "Junior")
print(se.name, se.age)
se.work()
se.debug()

d = Designer("Maciej", 28, 3500)
print(d.name, d.age)
d.work()
d.draw()


employees = [
    SoftwareEngineer("Mateusz", 33, 2500, "Junior"),
    Designer("Maciej", 28, 3500),
]


def employee_motivation(employees):
    for employee in employees:
        employee.work()


employee_motivation(employees)
