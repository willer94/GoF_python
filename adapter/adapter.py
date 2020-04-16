# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
from abc import ABCMeta, abstractmethod


class Print(metaclass=ABCMeta):
    @abstractmethod
    def printWeak(self):
        pass

    @abstractmethod
    def printStrong(self):
        pass


class Banner(object):
    def __init__(self, name):
        self.name = name

    def showWithParen(self):
        print('({})'.format(self.name))

    def showWithAster(self):
        print('*{}*'.format(self.name))


class BannerPrint(Print, Banner):
    def __init__(self, name):
        Banner.__init__(self, name)

    def printWeak(self):
        self.showWithAster()

    def printStrong(self):
        self.showWithAster()


if __name__ == '__main__':
    p = BannerPrint('hello')
    p.printWeak()
    p.printStrong()
