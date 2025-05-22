from cgi import print_exception
import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert isinstance(name, str) is True, f"Name variable {name} is not string."
        assert price >= 0.0, f"Price {price} is not positive number."
        assert quantity >= 0, f"Quantity {quantity} is not positive number."

        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long...")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @name.setter
    def name(self, value):
        self.__price = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * self.increment_value

    @classmethod
    def instance_from_csv(cls):
        with open("ExampleClass/OOP_with_freeCodeCamp/items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""Hello Someone.
        We have {self.name} {self.quantity} times.py
        Regards, Mateusz Sarnowski
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()


# Item.instance_from_csv()
# print(Item.all)
"""for instance in Item.all:
    print(f"Item name is: {instance.name}, price of item is: {instance.price}, and quantity this item is {instance.quantity}.")"""

# print(Item.is_integer(7.0))
# print(Item.is_integer(7.5))
# print(Item.is_integer(7.0))
# print(Item.is_integer(7))
# print(Item.is_integer("seven"))

"""phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)

print(Phone.all)"""
