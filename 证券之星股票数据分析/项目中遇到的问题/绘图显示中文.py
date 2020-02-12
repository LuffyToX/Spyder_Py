# -*- coding:utf-8 -*-
""" 解决绘图显示中文的问题 """

import matplotlib.pyplot as plt

plt.figure()
plt.title("统计")
plt.show()
# 标题显示为乱码，原因是标题默认输出英文，如果输出中文，要对字体进行调整

''' 解决中文显示问题 '''
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
plt.title("统计")
plt.show()
