import urllib.request

# 使用 urllib.request 的 urlretrieve()函数直接将对应信息写入本地文件
# urllib.request.urlretrieve(url, filename=本地文件地址)
file = r'C:\Users\Dell\Desktop\Program\learn_python\learn_spider\spider_base\02.html'
fhandle = urllib.request.urlretrieve(r"http://www.taobao.com", filename=file)

# urlretrieve 执行过程中，会产生一些缓存
# 如果想清除缓存，可以使用 urlcleanup() 函数
urllib.request.urlcleanup()
# 依旧没有爬取到图片
