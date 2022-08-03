# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/20 22:25
# @Software: PyCharm
def countSort(lst, max_count=100):
    """
    if a list consist of numbers in 0 ~ 100,
     you can use O(n) time cost to sort it
    :param lst:list
    :param max_count:int
    :return:None
    """
    count = [0 for _ in range(max_count+1)]
    for val in lst:
        count[val] += 1
    lst.clear()
    for ind, val in enumerate(count):
        for _ in range(val):
            lst.append(ind)


if __name__ == '__main__':
    import random

    lst = [random.randint(0, 100) for _ in range(1000)]
    print(lst)
    countSort(lst)
    print(lst)