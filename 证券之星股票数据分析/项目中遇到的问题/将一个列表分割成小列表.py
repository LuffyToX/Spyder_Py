# -*- coding:utf-8 -*-
""" 将一个列表分割成子列表为固定长度的嵌套列表 """

''' 法一 '''
def list_of_groups(init_list, childern_list_len):
    list_of_group = zip(*(iter(init_list),) *childern_list_len)
    end_list = [list(i) for i in list_of_group]
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list

lst = [i for i in range(15)]
print("原列表为：\n{0}".format(lst))
print("\n法一分割后的列表为：\n{0}".format(list_of_groups(lst, 2)))

''' 法二 '''
n = 3 # 大列表中几个数据组成一个小列表
result = [lst[i:i + n] for i in range(0, len(lst), n)]
print("\n法二分割后的列表为：\n{0}".format(result))