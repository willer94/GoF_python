# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
from abc import ABCMeta, abstractmethod
import copy


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self, string):
        pass

    @abstractmethod
    def createClone(self):
        pass


class Manager(object):
    def __init__(self):
        self.showcase = {}

    def register(self, name, proto):
        self.showcase[name] = proto

    def create(self, name):
        p = self.showcase[name]
        return p.createClone()


class MessageBox(Product):
    def __init__(self, ch):
        self.decochar = ch

    def use(self, s):
        l = len(s)
        print(''.join([self.decochar] * (l + 4)))
        print('{} {} {}'.format(self.decochar, s, self.decochar))
        print(''.join([self.decochar] * (l + 4)))

    def createClone(self):
        p = None
        try:
            p = MessageBox(copy.deepcopy(self.decochar))
        except Exception as e:
            print(e)
        return p


class UnderlinePan(Product):
    def __init__(self, ch):
        self.decochar = ch

    def use(self, s):
        l = len(s)
        print('" {} "'.format(s))
        print(''.join([self.decochar] * (l + 4)))

    def createClone(self):
        p = None
        try:
            p = UnderlinePan(copy.deepcopy(self.decochar))
        except Exception as e:
            print(e)
        return p


if __name__ == '__main__':
    manager = Manager()
    upen = UnderlinePan('~')
    mbox = MessageBox('*')
    sbox = MessageBox('/')
    manager.register('strong message', upen)
    manager.register('warning box', mbox)
    manager.register('slash box', sbox)

    p1 = manager.create('strong message')
    p1.use('Hellow, World.')
    p2 = manager.create('warning box')
    p2.use('Hellow, World.')
    p3 = manager.create('slash box')
    p3.use('Hello, World.')
