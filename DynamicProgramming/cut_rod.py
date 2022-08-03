# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/8/3 14:32
# @Software: PyCharm
import functools


global p
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]

@functools.lru_cache()
def cut_rod_recurision(n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurision(i) + cut_rod_recurision(n - i))
        return res

def cut_rod(n):
    r = [0]*(n+1)
    for j in range(1, n+1):
        q = 0
        for i in range(1, j+1):
            q = max(q, p[i]+r[j-i])
        r[j] = q
    return r[n]



if __name__ == '__main__':
    print(cut_rod_recurision(20))
    print(cut_rod(20))
