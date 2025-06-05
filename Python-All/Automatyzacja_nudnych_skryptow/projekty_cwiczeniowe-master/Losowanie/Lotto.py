import random


class Lotto:
    def get_list_of_numbers(self):
        list_of_numbers = []
        for i in range(0, 6):
            list_of_numbers.append(random.randint(1, 50))

        list_of_numbers.sort()
        return list_of_numbers
