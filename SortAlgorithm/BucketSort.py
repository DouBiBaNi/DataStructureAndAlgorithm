# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/20 23:07
# @Software: PyCharm
def bucketSort(lst, n=100, max_num=10000):
    """
    n is the number of buckets
    :param lst:list
    :param n:int
    :param max_num:int
    :return:None
    """
    buckets = [[] for _ in range(n)]
    for val in lst:
        i = min(val//(max_num//n), n-1)
        buckets[i].append(val)
        k = len(buckets[i]) - 1
        for j in range(k, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    lst.clear()
    for buc in buckets:
        lst.extend(buc)


if __name__ == '__main__':
    import random

    lst = [random.randint(0, 10000) for _ in range(10000)]
    bucketSort(lst)
    print(lst)
