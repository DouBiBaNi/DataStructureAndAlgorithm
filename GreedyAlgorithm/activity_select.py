# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/8/2 23:29
# @Software: PyCharm

activities = [(1,4), (3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
activities.sort(key=lambda x:x[1])

def activity_select(a):
    res = [a[0]]
    for s, e in activities[1:]:
        if s > res[-1][1]:
            res.append((s,e))
    return res

if __name__ == '__main__':
    print(activity_select(activities))