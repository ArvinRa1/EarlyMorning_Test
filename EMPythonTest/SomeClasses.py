# Task 8
import math
from collections import OrderedDict

from Utils import InvalidOperationException


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.width * self.length


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi


# Task 9
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __new__(cls, name, price):
        return "{} costs {} euro(s)".format(name, price)


# Task 10
class PhoneBook:

    def __init__(self):
        self.phonebook = dict()

    def add_number(self, name, number):
        """
       Add a contact or throw InvalidOperationException if it is already present
        :param number: an integer number
        :param name: a string
       """
        if name in self.phonebook.keys():
            raise InvalidOperationException
        else:
            self.phonebook[name] = number

    def del_number(self, name):

        """
        Delete a contact or throw InvalidOperationException if it is not present
        :param name: a string
        """
        if name not in self.phonebook.keys():
            raise InvalidOperationException
        else:
            del self.phonebook[name]

    def size(self):

        """
        :return: current size of PhoneBook
        """
        return len(self.phonebook)

    def get_all(self):

        """
        return: a string representation of all entries in the format 'name: number',
        merged and separated by ';' and a space. The entries should be sorted alphabetically
        """
        # The test is not compatible with other predefined methods in dictionary(Pyhton)
        dict1 = OrderedDict(sorted(self.phonebook.items()))
        s = str()
        for k, v in dict1.items():
            s += str(k) + ': ' + str(v) + "; "
        return s[:-2]
