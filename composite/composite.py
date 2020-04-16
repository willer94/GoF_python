# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    def __init__(self, abspath=''):
        self.abspath = '/' + self.getName()

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def getAbsPath(self, prefix=''):
        pass

    def add(self):
        raise Exception('Can not add entry!')

    @abstractmethod
    def printList(self, prefix=""):
        pass

    def __str__(self):
        return '{} ({})'.format(self.getName(), self.getSize())


class File(Entry):
    def __init__(self, name, size):
        self.name, self.size = name, size
        super(File, self).__init__()

    def getAbsPath(self):
        return self.abspath

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def printList(self, prefix=''):
        print('{}/{}'.format(prefix, self.__str__()))


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.directory = []
        super(Directory, self).__init__()

    def getName(self):
        return self.name

    def getSize(self):
        size = 0
        for it in self.directory:
            size += it.getSize()
        return size

    def getAbsPath(self):
        return self.abspath

    def printList(self, prefix=""):
        print('{}/{}'.format(prefix, self.__str__()))
        for it in self.directory:
            it.printList('{}/{}'.format(prefix, self.name))

    def add(self, entry):
        self.directory.append(entry)
        entry.abspath = '{}{}'.format(self.abspath, entry.abspath)


if __name__ == '__main__':
    try:
        print('Making root entries....')
        rootdir = Directory('root')
        bindir = Directory('bin')
        tmpdir = Directory('tmp')
        usrdir = Directory('usr')
        rootdir.add(bindir)
        rootdir.add(tmpdir)
        rootdir.add(usrdir)
        bindir.add(File('vi', 10000))
        bindir.add(File('latex', 20000))
        rootdir.printList()

        print()
        print('Making usr entries...')
        yuki = Directory('yuki')
        hanako = Directory('hanako')
        tomura = Directory('tomura')
        usrdir.add(yuki)
        usrdir.add(hanako)
        usrdir.add(tomura)
        yuki.add(File('diary.html', 100))
        yuki.add(File('Composite.java', 200))
        hanako.add(File('memo.ext', 300))
        tomura.add(File('game.doc', 400))
        tomura.add(File('junk.mail', 500))
        ff = File('ff.txt', 100)
        tomura.add(ff)
        rootdir.printList()
        print(ff.getAbsPath())
    except Exception as e:
        print(e)
