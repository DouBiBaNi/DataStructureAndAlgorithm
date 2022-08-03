# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/20 14:22
# @Software: PyCharm
def merge(lst, lo, mi, hi):
    """
    sort the sorted list[lo:mi+1] and list[mi+1:hi]
    :param lst: list
    :param lo: int
    :param mi: int
    :param hi: int
    :return: None
    """
    i, j = lo, mi + 1
    ltmp = []
    while i <= mi and j <= hi:
        if lst[i] < lst[j]:
            ltmp.append(lst[i])
            i += 1
        else:
            ltmp.append(lst[j])
            j += 1
    while i <= mi:
        ltmp.append(lst[i])
        i += 1
    while j <= hi:
        ltmp.append(lst[j])
        j += 1
    lst[lo:hi + 1] = ltmp

def mergeSort(lst, lo=0, hi=None):
    """
    use merge to sort the list
    time cost:O(nlogn)
    :param lst:list
    :param lo:int
    :param hi:int
    :return:None
    """
    if hi is None:
        hi = len(lst)-1

    if lo < hi:
        mid = (lo + hi) // 2
        mergeSort(lst,lo,mid)
        mergeSort(lst,mid+1,hi)
        merge(lst,lo, mid, hi)

if __name__ == '__main__':
    import random
    lst = [i for i in range(1000)]
    random.shuffle(lst)
    print(lst)
    mergeSort(lst)
    print(lst)