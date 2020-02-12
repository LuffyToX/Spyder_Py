import urllib.request
#import pprint

# 打开并爬取一个网页，将取到的网页赋给变量 file
file = urllib.request.urlopen(r"http://www.baidu.com")

data = file.read()
#pprint.pprint(data)   # 网站的 HTML 代码

# 将爬取到的网页以网页的形式保存在本地
# 以二进制写入模式打开本地文件
fhandle = open(r'C:\Users\Dell\Desktop\Program\learn_python\learn_spider\spider_base\01.html','wb')
fhandle.write(data)
fhandle.close()   # 此时该网页已经保存在本地，但网站的图片还没有爬取到

