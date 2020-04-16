# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
from abc import ABCMeta, abstractmethod
import sys


#-------------------abstract factory----------------------
class Item(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, caption):
        self.caption = caption


class Link(Item, metaclass=ABCMeta):
    def __init__(self, caption, url):
        super(Link, self).__init__(caption)
        self.url = url


class Tray(Item, metaclass=ABCMeta):
    def __init__(self, caption):
        super(Tray, self).__init__(caption)
        self.tray = []

    def add(self, item):
        self.tray.append(item)


class Page(metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []

    def add(self, item):
        self.content.append(item)

    @abstractmethod
    def makeHTML(self):
        pass

    def output(self):
        try:
            filename = self.title + '.html'
            with open(filename, 'w') as f:
                f.write(self.makeHTML())
            print('{} write finished!'.format(filename))
        except Exception as e:
            print(e)


class Factory(metaclass=ABCMeta):
    def getFactory(classname):
        factory = None
        try:
            # factory = eval(classname)
            factory = getattr(sys.modules[__name__], classname)()
        except Exception as e:
            print(e)
        return factory

    @abstractmethod
    def createLink(self, caption, url):
        pass

    @abstractmethod
    def createTray(self, caption):
        pass

    @abstractmethod
    def createPage(self, title, authot):
        pass


#----------------------list factory-------------------------
class ListLink(Link):
    def makeHTML(self):
        return ' <li><a href=\"{}\">{}</a></li>\n'.format(
            self.url, self.caption)


class ListTray(Tray):
    def makeHTML(self):
        buffer = []
        buffer.append('<li>\n')
        buffer.append('{}\n'.format(self.caption))
        buffer.append('<ul>\n')
        for it in self.tray:
            buffer.append(it.makeHTML())
        buffer.append('</ul>\n')
        buffer.append('</li>\n')
        return ''.join(buffer)


class ListPage(Page):
    def makeHTML(self):
        buffer = []
        buffer.append('<html><head><title>{}</title></head>\n'.format(
            self.title))
        buffer.append('<body\n')
        buffer.append('<h1>{}</h1/\n'.format(self.title))
        buffer.append('<ul>\n')
        for cont in self.content:
            buffer.append(cont.makeHTML())
        buffer.append('</ul>\n')
        buffer.append('<hr><address>{}</address>'.format(self.author))
        buffer.append('</body></html>\n')
        return ''.join(buffer)


class ListFactory(Factory):
    def createLink(self, caption, url):
        return ListLink(caption, url)

    def createTray(self, caption):
        return ListTray(caption)

    def createPage(self, title, author):
        return ListPage(title, author)


#----------------------Table factory-------------------------
class TableLink(Link):
    def makeHTML(self):
        return '<td><a href=\"{}\">{}</a></td>\n'.format(
            self.url, self.caption)


class TableTray(Tray):
    def makeHTML(self):
        buffer = []
        buffer.append('<td>')
        buffer.append('<table width=\"100%\" border=\"1\"<tr>')
        buffer.append('<td bgcolor=\"#cccccc\" align=\"center\" '\
                      'colspan=\"{}\"><b>{}</b></td>'.format(
                          len(self.tray),
                          self.caption
                      ))

        buffer.append('</tr>\n<tr>\n')
        for it in self.tray:
            buffer.append(it.makeHTML())
        buffer.append('</tr></table>')
        buffer.append('</td>')
        return ''.join(buffer)


class TablePage(Page):
    def makeHTML(self):
        buffer = []
        buffer.append('<html><head><title>{}</title></head>\n'.format(
            self.title))
        buffer.append('<body\n')
        buffer.append('<h1>{}</h1/\n'.format(self.title))
        buffer.append('<table width=\"80%\" border=\"3\">\n')
        for it in self.content:
            buffer.append(it.makeHTML())
        buffer.append('</table>\n')
        buffer.append('<hr><address>{}</address>'.format(self.author))
        buffer.append('</body></html>\n')
        return ''.join(buffer)


class TableFactory(Factory):
    def createLink(self, caption, url):
        return TableLink(caption, url)

    def createTray(self, caption):
        return TableTray(caption)

    def createPage(self, title, author):
        return TablePage(title, author)


if __name__ == '__main__':
    import argparse
    parse = argparse.ArgumentParser('python abstract factory')
    parse.add_argument('-c',
                       default='ListFactory',
                       type=str,
                       help='ListFactory or BoxFactory')
    args = parse.parse_args()

    factory = Factory.getFactory(args.c)

    people = factory.createLink('ren min ri bao', 'http://www.people.com.cn/')
    gmw = factory.createLink('guang ming ri bao', 'http://www.gmw.cn/')

    us_yahoo = factory.createLink('Yahoo!', 'http://www.yahoo.com/')
    jp_yahoo = factory.createLink('Yahoo!Japan', 'http://www.yahoo.com.jp/')
    excite = factory.createLink('Excite', 'http://www.excite.com/')
    baidu = factory.createLink('Baidu', 'http://www.baidu.com/')

    traynews = factory.createTray('newpapers')
    traynews.add(people)
    traynews.add(gmw)

    traysearch = factory.createTray('search engine')
    traysearch.add(us_yahoo)
    traysearch.add(jp_yahoo)
    traysearch.add(excite)
    traysearch.add(baidu)

    page = factory.createPage('LinkPage', 'wangzi')
    page.add(traynews)
    page.add(traysearch)
    page.output()
