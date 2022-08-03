# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/19 13:46
# @Software: PyCharm

# heap sort
# step 1. Build a heap
# step 2. Get the top element of the heap, which is the largest element
# step 3. Remove the top of the heap, put the last element of the heap on the top of the heap,
# and re-order the heap by one adjustment
# step 4. The top element of the heap is the second largest element
# step 5. Repeat step 3 until the heap becomes empty

def sift(lst, lo, hi):
    """
    Adjust the heap such that becoming maxheap
    time cost:O(nlogn)
    :param lst: list
    :param lo: int
    :param hi: int
    :return:None
    """
    i = lo
    j = 2 * i + 1       # left children
    temp = lst[lo]
    while j <= hi:      # the index no more than the last element of the heap
        if j + 1 <= hi and lst[j+1] > lst[j]: # right children is existing and larger
            j += 1      # direction to right children
        if lst[j] > temp:
            lst[i] = lst[j]
            i = j       # next level
            j = 2 * i + 1
        else:
            break
    lst[i] = temp

def heapSort(lst):
    n = len(lst)
    for i in range((n-2)//2, -1, -1): # i is the root of adjust heap
        sift(lst, i, n-1)
    # successfully build the maxheap
    for i in range(n-1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        sift(lst,0, i-1)


if __name__ == '__main__':
    lst = [i for i in range(100)]
    import random

    random.shuffle(lst)
    print(lst)
    heapSort(lst)
    print(lst)

# import random
# import heapq
# lst = [i for i in range(100)]
# random.shuffle(lst)
# heapq.heapify(lst)
# n = len(lst)
# for i in range(n):
#     print(heapq.heappop(lst), end=",")



