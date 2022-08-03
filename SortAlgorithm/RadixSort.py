# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/21 15:06
# @Software: PyCharm

def radixSort(lst):
    """
    stable sorting from low to high
    :param lst:lst
    :return: None
    """
    it = 0
    max_val = max(lst)
    while max_val:
        buckets = [[] for _ in range(10)]
        for val in lst:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)

        lst.clear()
        for buc in buckets:
            lst.extend(buc)
        it += 1
        max_val //= 10


if __name__ == '__main__':
    import random

    lst = list(range(10000+1))
    random.shuffle(lst)
    radixSort(lst)
    print(lst)