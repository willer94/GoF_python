# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
"""
Capture and restore an object's internal state.
With memento, we can add the following function:
- undo
- redo
- history
- snapshot
"""
import copy
import random
import time


class Memento(object):
    def __init__(self, money):
        self.money = money
        self.fruits = []

    def getMoney(self):
        return self.money

    def addFruits(self, fruit):
        self.fruits.append(fruit)

    def getFruits(self):
        return copy.deepcopy(self.fruits)


class Gamer(object):
    fruitsname = ['apple', 'grape', 'banana', 'orange']

    def __init__(self, money):
        self.money = money
        self.fruits = []

    def getMoney(self):
        return self.money

    def bet(self):
        dice = random.randint(1, 7)
        if dice == 1:
            self.money += 100
            print('money increase!')
        elif dice == 2:
            self.money /= 2
            print('money half!')
        elif dice == 6:
            f = self.getFruits()
            self.fruits.append(f)
            print('get fruits {}'.format(f))
        else:
            print('nothing')

    def getFruits(self):
        prefix = '' if random.randint(0, 2) != 0 else 'nice '
        fruit = Gamer.fruitsname[random.randint(0, 3)]
        return '{}{}'.format(prefix, fruit)

    def __str__(self):
        return '[money = {}, fruits = {}'.format(self.money, self.fruits)

    def createMemento(self):
        memento = Memento(self.money)
        for fruit in self.fruits:
            if fruit.startswith('nice'):
                memento.fruits.append(fruit)
        return memento

    def restoreMemento(self, memento):
        self.money = memento.money
        self.fruits = copy.deepcopy(memento.fruits)


if __name__ == '__main__':
    gamer = Gamer(100)
    memento = gamer.createMemento()
    for i in range(100):
        print('======={}'.format(i))
        print('now state: {}'.format(gamer))

        gamer.bet()
        print('with money: {}'.format(gamer.getMoney()))
        if gamer.getMoney() > memento.getMoney():
            print('money increase, thus save state.')
            memento = gamer.createMemento()
        elif gamer.getMoney() < memento.getMoney() / 2:
            print('money decrease, thus restore before state.')
            gamer.restoreMemento(memento)

        try:
            time.sleep(0.1)
        except InterruptedError as e:
            print(e)
        print()
