# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
###########################
# template method
# processing framework is defined in father class
# while concrete prcessing method is implemented in child class
from abc import ABCMeta, abstractmethod


class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()


class CarDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print("<<", end='')

    def print(self):
        print(self.ch, end='')

    def close(self):
        print(">>", end='\n')


class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string

    def open(self):
        self.printLine()

    def close(self):
        self.printLine()

    def print(self):
        print('|{}|'.format(self.string))

    def printLine(self):
        print('+' + ''.join(['-'] * len(self.string)) + '+')


if __name__ == '__main__':
    d1 = CarDisplay('H')
    d2 = StringDisplay('Hello, World.')
    d1.display()
    d2.display()
