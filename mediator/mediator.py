# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time: 
"""
Define an object that encapsulates how a set of objects interact.
Mediator promotes loose coupling by keeping objects from referring to
each other explicitly, and it lets you vary their interaction
independently.
I am not familar with gui in python, so this is just a simple 
program.
"""

class Mediator(object):
    def __init__(self):
        pass
    
    def createColleague(self):
        self._colleague1 = Colleague1(self)
        self._colleague2 = Colleague2(self)

    def colleagueChanged(self):
        pass


class Colleague1(object):
    def __init__(self, mediator):
        self.mediator = mediator


class Colleague2(object):
    def __init__(self, mediator):
        self.mediator = mediator


if __name__ == '__main__':
    mediator = Mediator()
