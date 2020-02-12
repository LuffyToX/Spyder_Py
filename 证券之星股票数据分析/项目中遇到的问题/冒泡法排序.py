# -*- coding:utf-8 -*-
""" 冒泡法排序 """
import random

lst = [random.randint(1, 100) for i in range(20)]
print("排序前：\n{}".format(lst))

for i in range(len(lst)-1):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print("\n由小到大排序后：\n{}".format(lst))
