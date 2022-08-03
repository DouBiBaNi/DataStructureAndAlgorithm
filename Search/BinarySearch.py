# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/15 21:21
# @Software: PyCharm
def binarySearch(lst, x, lo=0, hi=None):
    """
    find the index of x in lst, time cost: O(logn).
    :param lst: list
    :param x: int
    :param lo: int
    :param hi: int
    :return: int
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(lst)

    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            lo = mid
        else:
            hi = mid

    return -1

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 3
    i = binarySearch(lst, x)
    print("the index of %d in list is %d" % (x, i))
