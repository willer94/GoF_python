# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
from abc import ABCMeta, abstractmethod


class Trouble(object):
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def __str__(self):
        return '[Trouble {}]'.format(self.number)


class Support(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self._next = None

    def setNext(self, _next):
        self._next = _next
        return _next

    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif self._next:
            self._next.support(trouble)
        else:
            self.fail(trouble)

    def __str__(self):
        return '[{}]'.format(self.name)

    @abstractmethod
    def resolve(self, trouble):
        pass

    def done(self, trouble):
        print('{} is resolved by {}.'.format(trouble, self.__str__()))

    def fail(self, trouble):
        print('{} can not be solved.'.format(trouble))


class LimitSupport(Support):
    def __init__(self, name, limit):
        super(LimitSupport, self).__init__(name)
        self.limit = limit

    def resolve(self, trouble):
        return trouble.getNumber() < self.limit


class OddSuppoer(Support):
    def resolve(self, trouble):
        return int(trouble.getNumber()) % 2 != 0


class SpecialSuppor(Support):
    def __init__(self, name, number):
        super(SpecialSuppor, self).__init__(name)
        self.number = number

    def resolve(self, trouble):
        return trouble.getNumber() == self.number


class NoSupport(Support):
    def resolve(self, trouble):
        return False


if __name__ == '__main__':
    alice = NoSupport('Alice')
    bob = LimitSupport('Bob', 100)
    charlie = SpecialSuppor('Charlie', 429)
    diana = LimitSupport('Diana', 200)
    elmo = OddSuppoer('Elmo')
    fred = LimitSupport('Fred', 300)

    alice.setNext(bob).setNext(charlie).setNext(diana).setNext(elmo).setNext(
        fred)
    for i in range(0, 500, 33):
        alice.support(Trouble(i))
