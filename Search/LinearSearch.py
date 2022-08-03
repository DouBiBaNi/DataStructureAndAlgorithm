# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/15 20:33
# @Software: PyCharm

def linear_search(lst, x, lo=0, hi=None):
    """
    find the index in the lst, and return None if not find
    :param lst:list
    :param x:int
    :param lo:int
    :param hi:int
    :return:int
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(lst)

    flag = False
    for i, v in enumerate(lst[lo:hi]):
        if v == x:
            flag = True
            print("the index of %d in list is %d " % (x, i))
    if not flag:
        print("not find the %d in list" % x)

if __name__ == '__main__':
    lst = [2, 3, 5, 6, 7, 8, 4, 2, 3, 1]
    x = linear_search(lst, 2)

# result:
# the index of 2 in list is 0
# the index of 2 in list is 7