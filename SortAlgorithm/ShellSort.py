# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/20 18:53
# @Software: PyCharm
def insertSortGap(lst, gap):
    """
    when gap = 1: insert_sort
    :param lst: list
    :param gap: int
    :return: None
    """
    n = len(lst)
    for i in range(gap, n):
        temp = lst[i]
        j = i - gap
        while j >= 0 and lst[j] > temp:
            lst[j + gap] = lst[j]
            j -= gap
        lst[j + gap] = temp


def shellSort(lst):
    """
    time cost: O(nlog^2n)<= ? <= O(n^2)
    :param lst: list
    :return: None
    """
    n = len(lst)
    d = n // 2
    while d > 0:
        insertSortGap(lst, d)
        d //= 2


if __name__ == '__main__':
    import random

    lst = [i for i in range(1000)]
    random.shuffle(lst)
    print(lst)
    shellSort(lst)
    print(lst)
