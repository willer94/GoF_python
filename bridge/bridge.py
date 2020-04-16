# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
from abc import ABCMeta, abstractmethod
import random


class Display(object):
    def __init__(self, impl):
        self.impl = impl

    def open(self):
        self.impl.rawOpen()

    def close(self):
        self.impl.rawClose()

    def print(self):
        self.impl.rawPrint()

    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    def __init__(self, impl):
        super(CountDisplay, self).__init__(impl)

    def multiDisplay(self, times):
        self.open()
        for _ in range(times):
            self.print()
        self.close()


class DisplayImpl(metaclass=ABCMeta):
    @abstractmethod
    def rawOpen(self):
        pass

    @abstractmethod
    def rawPrint(self):
        pass

    @abstractmethod
    def rawClose(self):
        pass


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def rawOpen(self):
        self.printLines()

    def rawPrint(self):
        print('|{}|'.format(self.string))

    def rawClose(self):
        self.printLines()

    def printLines(self):
        print('+{}+'.format(''.join(['-'] * self.width)))


class RandomCountDisplay(CountDisplay):
    def randomTimeDisplay(self, times):
        self.multiDisplay(random.randint(0, times))


class CharDisplayImpl(DisplayImpl):
    def __init__(self, begin, body, foot):
        self.begin, self.body, self.foot = begin, body, foot

    def rawOpen(self):
        print(self.begin, end='')

    def rawClose(self):
        print(self.foot, end='\n')

    def rawPrint(self):
        print(self.body, end='')


class IncreaseCountDisplay(CountDisplay):
    def __init__(self, impl, step):
        super(IncreaseCountDisplay, self).__init__(impl)
        self.step = step

    def increaseCountDisplay(self, times):
        for ti in range(times):
            self.open()
            for st in range(ti * self.step):
                self.print()
            self.close()


if __name__ == '__main__':
    d1 = Display(StringDisplayImpl('Hello, China.'))
    d2 = CountDisplay(StringDisplayImpl('Hello, World.'))
    d3 = CountDisplay(StringDisplayImpl('Hello, Universe.'))
    d1.display()
    d2.display()
    d3.display()
    d3.multiDisplay(5)
    print()
    ###############################################
    d4 = RandomCountDisplay(StringDisplayImpl('Hello, China.'))
    d4.randomTimeDisplay(10)
    d4.randomTimeDisplay(10)
    print()
    ###############################################
    d5 = IncreaseCountDisplay(CharDisplayImpl('<','*','>'), 1)
    d6 = IncreaseCountDisplay(CharDisplayImpl('|', '#', '-'), 2)
    d5.increaseCountDisplay(4)
    d6.increaseCountDisplay(5)

