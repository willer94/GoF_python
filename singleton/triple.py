# -*- coding: utf-8 -*-
# Author: WangZi
# Mail: wangzitju@163.com
# Created Time:
class Triple(object):
    instance = []

    def __new__(cls):
        if len(cls.instance) < 3:
            cls.instance.append(super(Triple, cls).__new__(cls))
        return cls.instance[-1]

    def getInstance(self, id=0):
        return Triple.instance[int(id) % 3]


if __name__ == '__main__':
    tr1 = Triple()
    tr2 = Triple()
    tr3 = Triple()
    tr4 = Triple()

    print('tr1 and tr2 are same obj: {}'.format(tr1 is tr2))
    print('tr2 and tr3 are same obj: {}'.format(tr2 is tr3))
    print('tr1 and tr4 are same obj: {}'.format(tr1 is tr4))
    print('tr3 and tr4 are same obj: {}'.format(tr3 is tr4))

    print('t1 and getId 1:{}'.format(tr1 is tr4.getInstance(0)))
    print('t1 and getId 2:{}'.format(tr1 is tr4.getInstance(1)))
