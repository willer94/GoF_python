# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
from abc import ABCMeta, abstractmethod


class Display(metaclass=ABCMeta):
    @abstractmethod
    def getColumns(self):
        pass

    @abstractmethod
    def getRows(self):
        pass

    @abstractmethod
    def getRowText(self, i):
        pass

    def show(self):
        for i in range(self.getRows()):
            print(self.getRowText(i))


class StringDisplay(Display):
    def __init__(self, string):
        self.string = string

    def getColumns(self):
        return len(self.string)

    def getRows(self):
        return 1

    def getRowText(self, row):
        if row == 0:
            return self.string
        else:
            return None


class Border(Display):
    def __init__(self, display):
        self.display = display


class SideBorder(Border):
    def __init__(self, display, ch):
        super(SideBorder, self).__init__(display)
        self.borderChar = ch

    def getColumns(self):
        return 2 + self.display.getColumns()

    def getRows(self):
        return self.display.getRows()

    def getRowText(self, row):
        return '{}{}{}'.format(self.borderChar, self.display.getRowText(row),
                               self.borderChar)


class FullBorder(Border):
    def __init__(self, display):
        self.display = display

    def getColumns(self):
        return 2 + self.display.getColumns()

    def getRows(self):
        return 2 + self.display.getRows()

    def getRowText(self, row):
        if row == 0 or row == self.display.getRows() + 1:
            return '+{}+'.format(self.makeLine('-', self.display.getColumns()))
        else:
            return '|{}|'.format(self.display.getRowText(row - 1))

    def makeLine(self, ch, count):
        return ''.join([ch] * count)


if __name__ == '__main__':
    b1 = StringDisplay('Hello, World.')
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)

    b1.show()
    b2.show()
    b3.show()
