# -*- coding:utf-8 -*-
""" 去除列表中的空字符以及 '\n' """

list = ['hello,world!', '    \n   ', 'Python', '', '\n', '中国\n']
print(list)

#result = [x.strip() for x in list if x.strip() != '']
result = []
for string in list:
    if string.strip() != '': # '    \n   ', '', '\n' 执行.strip()方法后都是 ''
        #result.append(string) 会输出 '中国\n'项
        result.append(string.strip())

print(result)