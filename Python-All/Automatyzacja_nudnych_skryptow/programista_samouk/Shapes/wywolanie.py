#!/usr/bin/python3


def equal(object_1, object_2):
    if object.__repr__(object_1) == object.__repr__(object_2):
        return True
    else:
        return False


class Shape:
    shape_list = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.shape_list.append((self.width, self.length))

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.length

    def what_am_i(self):
        print("Jestem Figurą!")


class Rectangle(Shape):
    def __repr__(self):
        return "Prostokąt: " + str(self.width) + " na " + str(self.length) + "."


class Square(Shape):
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append((self.side))

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, s):
        self.side = s

    def __repr__(self):
        return "Kwadrat: " + str(self.side) + " na " + str(self.side) + "."


rectangle_1 = Rectangle(10, 456)
square_1 = Square(88)

print("Długość obwodu mojego prostokąta: ", rectangle_1.calculate_perimeter(), ".")
rectangle_1.what_am_i()
print("I długość obwodu mojego kwadratu: ", square_1.calculate_perimeter(), ".")
square_1.what_am_i()
print(square_1)

square_1.change_size(111)

print(
    "Po zmianie długości boku kwadratu na 111, długość obwodu, to: ",
    square_1.calculate_perimeter(),
    ".",
)
square_1.what_am_i
print(square_1)

print(
    "Porównanie kwadratu o boku 111, z tym samym kwadratem: "
    + str(equal(square_1, square_1))
)
print(
    "Porównanie kwadratu o boku 111, z prostokątem: "
    + rectangle_1.__repr__()
    + " "
    + str(equal(square_1, rectangle_1))
)
