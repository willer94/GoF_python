# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
####################################################
# builder is used to assemble instances with complex
# construction. I skip over html builder here. 
from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def makeTitle(self, title: str):
        pass

    @abstractmethod
    def makeString(self, string: str):
        pass

    @abstractmethod
    def makeItems(self, items: list):
        pass

    @abstractmethod
    def close(self):
        pass


class Director(object):
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        builder = self.builder
        builder.makeTitle("Greeting.")
        builder.makeString("From morning to afternoon.")
        builder.makeItems(["Good morning.", "Good afternoon."])
        builder.makeString('Evening.')
        builder.makeItems(["Good evening.", "Good night.", "See you."])
        builder.close()


class TextBuilder(Builder):
    def __init__(self):
        self.buffer = ''

    def makeTitle(self, title):
        self.buffer += '====================================\n'
        self.buffer += '[{}]\n\n'.format(title)

    def makeString(self, string):
        self.buffer += '-{}\n\n'.format(string)

    def makeItems(self, items):
        for item in items:
            self.buffer += '\t*{}\n'.format(item)
        self.buffer += '\n'

    def close(self):
        self.buffer += '====================================\n'

    def getResult(self):
        return self.buffer


if __name__ == '__main__':
    textbuilder = TextBuilder()
    textdirector = Director(textbuilder)
    textdirector.construct()
    print(textbuilder.getResult())
    print(textbuilder is textdirector.builder)
