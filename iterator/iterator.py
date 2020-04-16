from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def iterator(self):
        pass


class Book(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class BookShelf(Aggregate):
    def __init__(self):
        super(BookShelf, self).__init__()
        self._books = []
        self._last = 0

    def getBookAt(self, id):
        return self._books[id]

    def appendBook(self, book):
        self._books.append(book)
        self._last += 1

    def getLength(self):
        return self._last

    def iterator(self):
        return BookShelfIter(self)


class BookShelfIter(Iterator):
    def __init__(self, bookshelf):
        super(BookShelfIter, self).__init__()
        self.bookshelf = bookshelf
        self.index = 0

    def hasNext(self):
        return self.index < self.bookshelf.getLength()

    def next(self):
        tmp = self.bookshelf.getBookAt(self.index)
        self.index += 1
        return tmp


class BookShelfv2(object):
    """python style iterator
    """
    def __init__(self):
        self._books = []

    def appendBook(self, book):
        self._books.append(book)

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __next__(self):
        return next(self._books)

    def __getitem__(self, id):
        return self._books[id]


if __name__ == '__main__':
    bookshelf1 = BookShelf()
    bookshelf1.appendBook(Book('Around the World in 80 Days'))
    bookshelf1.appendBook(Book('Bible'))
    bookshelf1.appendBook(Book('Cinderella'))
    bookshelf1.appendBook(Book('Daddy-Long-Legs'))
    it = bookshelf1.iterator()
    while it.hasNext():
        print(it.next().getName())

    print('\npython style iterator')
    bookshelf2 = BookShelfv2()
    bookshelf2.appendBook(Book('Around the World in 80 Days'))
    bookshelf2.appendBook(Book('Bible'))
    bookshelf2.appendBook(Book('Cinderella'))
    bookshelf2.appendBook(Book('Daddy-Long-Legs'))
    for it in bookshelf2:
        print(it.getName())
