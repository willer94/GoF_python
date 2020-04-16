# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
"""
https://sourcemaking.com/design_patterns/command/cpp/3
in python.
"""
from abc import ABCMeta, abstractmethod


class Number(object):
    def dubble(self, value):
        return 2 * value


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, num):
        pass


class SimpleCommand(Command):
    def __init__(self, rec):
        self.reciver = rec

    def execute(self, num):
        return self.reciver.dubble(num)


class MacroCommand(Command):
    def __init__(self):
        self.commands = []

    def add(self, cmd):
        self.commands.append(cmd)

    def execute(self, num):
        for cmd in self.commands:
            num = cmd.execute(num)
        return num


if __name__ == '__main__':
    obj = Number()
    macrotwo = MacroCommand()
    cmd1 = SimpleCommand(obj)
    macrotwo.add(cmd1)
    macrotwo.add(cmd1)
    macrofour = MacroCommand()
    macrofour.add(macrotwo)
    macrofour.add(macrotwo)

    cmd = [cmd1, macrotwo, macrofour]
    while True:
        print('Enter number selection: (0=2x, 1=4x, 2=16x)')
        tmp = input()
        tmp = [item for item in tmp.split() if item != ' ']
        try:
            num = int(tmp[0])
            index = int(tmp[1])
            print(cmd[index].execute(num))
        except ValueError as e:
            print(e)
            break
