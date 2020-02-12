# -*- coding:utf-8 -*-
""" 解决使用 plt.save 保存图片时一片空白 """

import os
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\Dell\Desktop')
x = [i for i in range(10)]
y = [i**2 for i in range(10)]
plt.plot(x, y)

#plt.show()
#plt.savefig("example.png")
'''
原因：
在 plt.show() 后实际上已经创建了一个新的空白的图片（坐标轴），
这时候再 plt.savefig() 就会保存这个新生成的空白图片
'''
plt.savefig("example.png")
plt.show()