# 爬取链接地址
import re
import urllib.request

def getlink(url):
    # 模拟成浏览器
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    # 将 opener 安装为全局
    urllib.request.install_opener(opener)

    # 打开并读取网页源代码
    data = str(urllib.request.urlopen(url).read())

    # 构建好相应的正则表达式
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)

    # 去除重复元素并返回列表
    link = list(set(link))
    return link

# 要爬取的网页链接
url = "http://blog.csdn.net/"

# 获取对应网页中包含的链接地址
linklist = getlink(url)
for link in linklist:
    print(link[0])