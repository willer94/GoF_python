import abc


class Product(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def use(self):
        pass


class Factory(metaclass=abc.ABCMeta):
    def create(self, owner):
        p = self.createProduct(owner)
        self.registerProduct(p)
        return p

    @abc.abstractmethod
    def createProduct(self, owner):
        pass

    @abc.abstractmethod
    def registerProduct(self, product):
        pass


class IDCard(Product):
    def __init__(self, owner):
        super(IDCard, self).__init__()
        self.owner = owner

    def use(self):
        print("use {}'s IDcard".format(self.owner))

    def getOwner(self):
        return self.owner


class IDcardFactory(Factory):
    def __init__(self):
        super(IDcardFactory, self).__init__()
        self.owners = []

    def createProduct(self, owner):
        return IDCard(owner)

    def registerProduct(self, product):
        self.owners.append(product.getOwner())

    def getOwners(self):
        return self.owners


if __name__ == '__main__':
    fac = IDcardFactory()
    card1 = fac.create('jane')
    card2 = fac.create('tom')
    card3 = fac.create('mike')
    card1.use()
    card2.use()
    card3.use()
    print(fac.getOwners())
