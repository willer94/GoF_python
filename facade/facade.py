# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
class Properties(object):
    def __init__(self, ch='='):
        self.ch = ch
        self.properties = {}

    def load(self, f):
        content = f.readlines()
        content = [item.strip() for item in content]
        for item in content:
            a, b = item.split(self.ch)
            self.properties[a] = b

    def getProperty(self, a):
        return self.properties[a]


class Database(object):
    @classmethod
    def getProperty(cls, dbname):
        with open(dbname + '.txt', 'r') as f:
            prop = Properties()
            try:
                prop.load(f)
            except Exception as e:
                print(e)
        return prop


class HtmlWriter(object):
    def __init__(self, writer):
        self.writer = writer

    def title(self, title):
        try:
            self.writer.write('<html>')
            self.writer.write('<head>')
            self.writer.write('<title>{}</title>'.format(title))
            self.writer.write('</head><body>\n')
            self.writer.write('<h1>{}</h1>\n'.format(title))
        except IOError as e:
            return e

    def paragraph(self, msg):
        try:
            self.writer.write('<p>{}</p>\n'.format(msg))
        except IOError as e:
            return e

    def link(self, href, caption):
        try:
            self.writer.write('<a href=\"{}\">{}</a>'.format(href, caption))
        except IOError as e:
            return e

    def mailto(self, mailaddr, username):
        try:
            self.link('mailto: {}'.format(mailaddr), username)
        except IOError as e:
            return e

    def close(self):
        try:
            self.writer.write('</body>')
            self.writer.write('</html>\n')
            self.writer.close()
        except IOError as e:
            return e


class PageMaker(object):
    @classmethod
    def makeWelcomePage(cls, mailaddr, filename):
        try:
            mailprop = Database.getProperty('maildata')
            username = mailprop.getProperty(mailaddr)
            with open(filename, 'w') as f:
                writer = HtmlWriter(f)
                writer.title('Welcome to {}\' page!')
                writer.paragraph('{} welcome {}\'s page'.format(
                    username, username))
                writer.paragraph('waiting for your email.')
                writer.mailto(mailaddr, username)
                writer.close()

                print('{} is created for {} ({})'.format(
                    filename, mailaddr, username))
        except IOError as e:
            print(e)


if __name__ == '__main__':
    PageMaker.makeWelcomePage('hyuki@hyuki.com', 'welcome.html')
