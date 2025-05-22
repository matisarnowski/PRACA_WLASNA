#!/usr/bin/python3


class SoftwareEngineer:
    pass

    def __init__(self):
        self._value = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary
