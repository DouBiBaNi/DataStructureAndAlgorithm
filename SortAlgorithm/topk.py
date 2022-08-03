# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/20 11:39
# @Software: PyCharm
def minHeap(lst, lo=0 , hi=None):
    if hi is None:
        hi = len(lst)-1

    i = lo
    j = 2 * i + 1
    temp = lst[lo]
    while j <= hi:
        if j + 1 <= hi and lst[j+1] < lst[j]:
            j += 1
        if lst[j] < temp:
            lst[i] = lst[j]
            i = j
            j = 2 * i + 1
        else:
            break
    lst[i] = temp

def topk(lst, k):
    heap = lst[0:k]
    # build minheap
    for i in range((k-2)//2, -1, -1):
        minHeap(heap, i, k-1)

    # traverse
    for i in range(k, len(lst)):
        if heap[0] < lst[i]:
            heap[0]= lst[i]
            minHeap(heap)
    # print(heap)

    # outcome
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        minHeap(heap, 0, i-1)
    return heap

if __name__ == '__main__':
    import random
    lst = [i for i in range(1000)]
    random.shuffle(lst)
    print(topk(lst,10))

