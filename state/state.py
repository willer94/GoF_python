# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
"""
Allow an object alter its behavior when its interal state changes.
The object will appear to change its class.

How to define state classes:
- Define API, declare abstract methods.
- Define multi classes, implement concrete methods.
state classes usually use sinleton pattern.
"""
from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    INSTANCE = None

    def __new__(cls):
        if not cls.INSTANCE:
            cls.INSTANCE = object.__new__(cls)
        return cls.INSTANCE

    @abstractmethod
    def handle(self):
        pass


class ConcreteState1(State):
    def __new__(cls):
        super(ConcreteState1, cls).__new__(cls)
        return cls.INSTANCE

    def handle(self):
        pass


class ConcreteState2(State):
    def __new__(cls):
        super(ConcreteState2, cls).__new__(cls)
        return cls.INSTANCE

    def handle(self):
        pass


class Context(object):
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

    def changeState(self, th):
        if th < 10:
            self._state = ConcreteState1()
        else:
            self._state = ConcreteState2()


if __name__ == '__main__':
    state1 = ConcreteState1()
    state2 = ConcreteState2()
    state3 = ConcreteState2()
    print(state1 is state2)
    print(state3 is state2)
    print(type(state1), type(state2), type(state3))
