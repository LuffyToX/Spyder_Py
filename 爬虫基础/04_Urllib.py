import urllib.request

url = r'https://www.jianshu.com/p/a6549fd7c951'

# 存储 User-Agent 信息
# ("User-Agent", 具体信息)
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400")

# 创建 bulid_opener 对象
opener = urllib.request.build_opener()

# 设置头信息
# bulid_opener对象名.addheaders = [头信息]
opener.addheaders = [headers]

# 打开网址并读取
# bulid_opener对象名.open(url地址).read()
data = opener.open(url).read()

fhandle = open(r'C:\Users\Dell\Desktop\Program\learn_python\learn_spider\spider_base\04.html','wb')
fhandle.write(data)
fhandle.close()
