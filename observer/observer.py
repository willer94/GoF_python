# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
"""
A way to notify changes to multi clases.
"""
from abc import ABCMeta, abstractmethod
import random
import time


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, generator):
        pass


class NumberGenerator(metaclass=ABCMeta):
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def deleteObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for ob in self.observers:
            ob.update(self)

    @abstractmethod
    def getNumber(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        super(RandomNumberGenerator, self).__init__()
        self.number = None

    def getNumber(self):
        return self.number

    def execute(self):
        for _ in range(20):
            self.number = random.randint(0, 50)
            self.notifyObservers()


class IncrementalNumberGenerator(NumberGenerator):
    def __init__(self, begin, end, step):
        super(IncrementalNumberGenerator, self).__init__()
        self.begin, self.end, self.step = begin, end, step
        self.number = None

    def getNumber(self):
        return self.number

    def execute(self):
        for num in range(self.begin, self.end, self.step):
            self.number = num
            self.notifyObservers()


class DigitObserver(Observer):
    def update(self, generator):
        print('DigitObserver: {}'.format(generator.getNumber()))
        try:
            time.sleep(0.1)
        except InterruptedError as e:
            print(e)


class GraphObserver(Observer):
    def update(self, generator):
        print('GraphObserver: {}'.format(''.join(['*'] *
                                                 generator.getNumber())))
        try:
            time.sleep(0.1)
        except InterruptedError as e:
            print(e)


if __name__ == '__main__':
    generator = RandomNumberGenerator()
    observer1, observer2 = DigitObserver(), GraphObserver()
    generator.addObserver(observer1)
    generator.addObserver(observer2)
    generator.execute()

    print('--------------------------------------------')
    generator1 = IncrementalNumberGenerator(10, 50, 5)
    generator1.addObserver(observer1)
    generator1.addObserver(observer2)
    generator1.execute()
