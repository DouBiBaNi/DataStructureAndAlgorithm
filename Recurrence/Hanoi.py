# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/15 12:45
# @Software: PyCharm
"""
汉诺塔问题：已知有A、B、C三个柱子，A柱子上有n个石块大到小依次堆叠，计算如何将其所有石头移到另一个柱子B或C上。
"""


class Hanoi():

    def __init__(self, n=3):
        self.n = n
        self.a = "A"
        self.b = "B"
        self.c = "C"
        self.times = 0

    def run(self):
        def hanoi(n, a, b, c):
            if n > 0:
                hanoi(n - 1, a, c, b)
                self.times += 1
                print("move %s to %s" % (a, c))
                hanoi(n - 1, b, a, c)
            return

        hanoi(n=self.n, a=self.a, b=self.b, c=self.c)
        print("Total moving: %d" % self.times)


if __name__ == '__main__':
    hanoi1 = Hanoi(4)
    hanoi1.run()
#    result:
    # move A to B
    # move A to C
    # move B to C
    # move A to B
    # move C to A
    # move C to B
    # move A to B
    # move A to C
    # move B to C
    # move B to A
    # move C to A
    # move B to C
    # move A to B
    # move A to C
    # move B to C
    # Total moving: 15
