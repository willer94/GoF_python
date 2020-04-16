# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, file):
        pass


class Entry(metaclass=ABCMeta):
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    def accept(self, visitor):
        raise Exception('File Treatment Exception.')

    def add(self):
        raise Exception('File Treatment Exception.')

    def __str__(self):
        return '{} ({})'.format(self.getName(), self.getSize())


class File(Entry):
    def __init__(self, name, size):
        self.name, self.size = name, size

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def accept(self, visitor):
        visitor.visit(self)


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.dir = []

    def getName(self):
        return self.name

    def getSize(self):
        size = 0
        for it in self.dir:
            size += it.getSize()
        return size

    def __iter__(self):
        return iter(self.dir)

    def add(self, entry):
        self.dir.append(entry)

    def accept(self, visitor):
        visitor.visit(self)


class ListVisitor(Visitor):
    def __init__(self):
        self.currentdir = ""

    def visit(self, entry):
        if isinstance(entry, File):
            print('{}/{}'.format(self.currentdir, entry))
        else:
            print('{}/{}'.format(self.currentdir, entry))
            savedir = self.currentdir
            self.currentdir = '{}/{}'.format(self.currentdir, entry.getName())
            for it in entry:
                self.visit(it)
            self.currentdir = savedir


class FileFindVisitor(Visitor):
    def __init__(self, suffix):
        self.currentdir = ''
        self.suffix = suffix
        self.FoundFiles = []

    def visit(self, entry):
        if isinstance(entry, File):
            if entry.getName().split('.')[-1] == self.suffix:
                self.FoundFiles.append('{}/{}'.format(self.currentdir, entry))
        else:
            savedir = self.currentdir
            self.currentdir = '{}/{}'.format(self.currentdir, entry.getName())
            for it in entry:
                self.visit(it)
            self.currentdir = savedir

    def getFoundFiles(self):
        return self.FoundFiles


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
        rootdir.accept(ListVisitor())

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
        tomura.add(File('junk.html', 800))
        ff = File('ff.txt', 100)
        tomura.add(ff)
        rootdir.accept(ListVisitor())

        print('---------------------------------')
        print('get all html files')
        htmlfinder = FileFindVisitor('html')
        rootdir.accept(htmlfinder)
        for it in htmlfinder.getFoundFiles():
            print(it)
    except Exception as e:
        print(e)
