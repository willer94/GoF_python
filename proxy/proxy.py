# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
"""
Provide a surrogate or placeholder for another object to 
control access to it.
Use an extra level of indirection to support distributed,
controlled, or intelligent acces.
Add a wrapper and delegation to protect the real component 
from undue complexity.
"""
from abc import ABCMeta, abstractmethod
import time


class Printable(metaclass=ABCMeta):
    @abstractmethod
    def setPrinterName(self, name):
        pass

    @abstractmethod
    def getPrinterName(self):
        pass

    @abstractmethod
    def print(self, string):
        pass


class Printer(Printable):
    def __init__(self, name=''):
        suffix = ''
        self.name = name
        if not name:
            suffix = '({})'.format(name)
        self.heavyJob('Printer\'s instance is creaing {}'.format(suffix))

    def setPrinterName(self, name):
        self.name = name

    def getPrinterName(self):
        return self.name

    def print(self, string):
        print('============{}============='.format(self.name))
        print(string)

    def heavyJob(self, msg):
        print(msg)
        for i in range(5):
            try:
                time.sleep(1)
            except InterruptedError as e:
                print(e)
            print('.')
        print('End.')


class PrinterProxy(Printable):
    def __init__(self, name=None):
        self.name = name
        self.real = None

    def setPrinterName(self, name):
        self.name = name

    def getPrinterName(self):
        return self.name

    def print(self, string):
        self.realize()
        self.real.print(string)

    def realize(self):
        if not self.real:
            self.real = Printer(self.name)


if __name__ == '__main__':
    p = PrinterProxy('Alice')
    print('Now name is: {}.'.format(p.getPrinterName()))
    p.setPrinterName('Bob')
    print('Now name is: {}.'.format(p.getPrinterName()))
    p.print('Hello, World.')
