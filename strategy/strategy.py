# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
from abc import ABCMeta, abstractmethod
import random


class Hand(object):
    HANDVALUES = ['GUU', 'CHO', 'PAA']
    lab2name = {i: item for i, item in enumerate(HANDVALUES)}
    name2lab = {item: i for i, item in enumerate(HANDVALUES)}

    def __init__(self, handvalue):
        self.handvalue = handvalue

    @staticmethod
    def getHand(handvalue):
        return Hand(handvalue)

    def isStrongerThan(self, h):
        return self.fight(h) == 1

    def isWeakerThan(self, h):
        return self.fight(h) == -1

    def fight(self, h):
        if self.handvalue == h.handvalue:
            return 0
        elif (self.handvalue + 1) % 3 == h.handvalue:
            return 1
        else:
            return -1

    def toString(self):
        return Hand.lab2name[self.handvalue]


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def nextHand(self):
        pass

    @abstractmethod
    def study(self, win):
        pass


class WinningStrategy(Strategy):
    def __init__(self):
        super(WinningStrategy, self).__init__()
        self.won = False
        self.prevHand = None

    def nextHand(self):
        if not self.won:
            self.prevHand = Hand.getHand(random.randint(0, 3))
        return self.prevHand

    def study(self, win):
        self.won = win


class ProbStrategy(Strategy):
    def __init__(self):
        super(ProbStrategy, self).__init__()
        self.prevHandValue = 0
        self.currentHandValue = 0
        self.history = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]

    def nextHand(self):
        bet = random.randint(0, self.getSum(self.currentHandValue))
        handvalue = 0
        if bet < self.history[self.currentHandValue][0]:
            handvalue = 0
        elif bet < self.history[self.currentHandValue][0] + \
            self.history[self.currentHandValue][1]:
            handvalue = 1
        else:
            handvalue = 2
        prevHandValue = self.currentHandValue
        self.currentHandValue = handvalue
        return Hand.getHand(handvalue)

    def getSum(self, hv):
        _sum = 0
        for i in range(3):
            _sum += self.history[hv][i]
        return _sum

    def study(self, win):
        if win:
            self.history[self.prevHandValue][self.currentHandValue] += 1
        else:
            self.history[self.prevHandValue][(self.currentHandValue + 1) %
                                             3] += 1
            self.history[self.prevHandValue][(self.currentHandValue + 2) %
                                             3] += 1


class Player(object):
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.wincount = 0
        self.losecount = 0
        self.gamecount = 0

    def nextHand(self):
        return self.strategy.nextHand()

    def win(self):
        self.strategy.study(True)
        self.wincount += 1
        self.gamecount += 1

    def lose(self):
        self.strategy.study(False)
        self.losecount += 1
        self.gamecount += 1

    def even(self):
        self.gamecount += 1

    def __str__(self):
        return '[{}: {} games, {} win, {} lose]'.format(
            self.name, self.gamecount, self.wincount, self.losecount)


if __name__ == '__main__':
    player1 = Player('Taro', WinningStrategy())
    player2 = Player('Hana', ProbStrategy())

    for gameId in range(10000):
        nexthand1, nexthand2 = player1.nextHand(), player2.nextHand()
        print('{}: '.format(gameId), end='')
        if nexthand1.isStrongerThan(nexthand2):
            player1.win()
            player2.lose()
            print('Winner: {}'.format(player1.name))
        elif nexthand2.isStrongerThan(nexthand1):
            player1.lose()
            player2.win()
            print('Winner: {}'.format(player2.name))
        else:
            player1.even()
            player2.even()
            print('Even')

    print('Total result')
    print(player1)
    print(player2)
