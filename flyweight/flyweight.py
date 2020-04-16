# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
class BigChar(object):
    def __init__(self, charname):
        self.charname = charname
        try:
            with open('big{}.txt'.format(charname), 'r') as f:
                buf = f.readlines()
            self.fontdata = ''.join(buf)
        except IOError as e:
            self.fontdata = charname + '?'

    def print(self):
        print(self.fontdata)


class BigCharFactory(object):
    pool = {}
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

    @classmethod
    def getInstance(cls):
        cls.__new__(cls)
        return cls.instance

    def getBigChar(self, charname):
        if charname in BigCharFactory.pool.keys():
            return BigCharFactory.pool[charname]
        bc = BigChar(charname)
        BigCharFactory.pool[charname] = bc
        return bc


class BigString(object):
    def __init__(self, string, shared=True):
        self.bigchars = []
        if shared:
            factory = BigCharFactory.getInstance()
            for ss in string:
                self.bigchars.append(factory.getBigChar(ss))
        else:
            for ss in string:
                self.bigchars.append(BigChar(ss))

    def print(self):
        for ss in self.bigchars:
            ss.print()


def main_shared():
    bs = BigString(''.join(['1'] * 100))
    bs.print()


def main_not_shared():
    bs = BigString(''.join(['1'] * 100))
    bs.print()


if __name__ == '__main__':
    main_not_shared()
    main_shared()
