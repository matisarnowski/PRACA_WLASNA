#!/usr/bin/python3


class Customer:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership


customers = [
    Customer("Maciej", "Gold"),
    Customer("Mateusz", "Bronze"),
    Customer("Jakub", "Silver"),
]

print("Imona użytkowników, to:")
for i in range(0, len(customers)):
    if i != len(customers) - 1:
        print(customers[i].name + ", ")
    else:
        print(customers[i].name + ".")
