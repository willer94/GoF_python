# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
class Singleton(object):
    INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls.INSTANCE:
            cls.INSTANCE = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.INSTANCE

    def __init__(self, *args, **kwargs):
        pass


class TicketMaker(object):
    def __init__(self):
        self.ticket = 1000

    def getNextTicketNumber(self):
        a = self.ticket
        self.ticket += 1
        return a


class TicketMakerSingleton(object):
    INSTANCE = None

    def __new__(cls):
        if not cls.INSTANCE:
            cls.INSTANCE = TicketMaker()
        return cls.INSTANCE


class TicketMakerSingleton2(TicketMaker):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = TicketMaker()
        return cls.instance


if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()
    print(type(obj1), type(obj2))
    if obj1 is obj2:
        print('obj1 and obj2 are same instance')
    else:
        print('obj2 and obj2 are not same instance')

    print('---------------------')
    ticketmaker1 = TicketMakerSingleton()
    ticketmaker2 = TicketMakerSingleton()
    print(type(ticketmaker1), type(ticketmaker2))
    if ticketmaker1 is ticketmaker2:
        print('same object')
    else:
        print('not same')
    for _ in range(7):
        print(ticketmaker1.getNextTicketNumber(), end=', ')
    print()
    for _ in range(9):
        print(ticketmaker2.getNextTicketNumber(), end=', ')
    print()
    print('---------------------')
    tm1 = TicketMakerSingleton2()
    tm2 = TicketMakerSingleton2()
    print(type(tm1), type(tm2))
    print(tm1.getNextTicketNumber())
    print(tm2.getNextTicketNumber())
