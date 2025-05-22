import math
import numpy as np


class Matrix_main:
    def __init__(self, numbers, matrix=[]):
        self.numbers = numbers
        self.matrix = matrix

    def is_matrix_square(self):
        if math.sqrt(len(self.numbers)) > 0:
            numbers_in_matrix = len(self.numbers)
            while numbers_in_matrix > 0:
                count = 1
                numbers_in_matrix = numbers_in_matrix - count
                count = 2 * count - 1
            if numbers_in_matrix == 0:
                return True
            else:
                return False

    def to_matrix(self):
        shape = (int(math.sqrt(len(self.numbers))), int(math.sqrt(len(self.numbers))))
        if self.is_matrix_square():
            self.matrix = np.array(self.numbers)
            self.matrix = self.matrix.reshape(shape)
            return self.matrix
        else:
            self.matrix = []
            return self.matrix
