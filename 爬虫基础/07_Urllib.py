import urllib.request

# 关键词
key_word = "hello"

# 使用GET请求的 url 网址
# "https://.../s?wd="
# wd 是待检索关键词字段（百度）
url = "http://www.baidu.com/s?wd=" + key_word

# Request 对象
req = urllib.request.Request(url)

# 以 GET 请求的方式获取页面并读取页面内容
data = urllib.request.urlopen(req).read()

fh = open(r'C:\Users\Dell\Desktop\Program\learn_python\learn_spider\spider_base\07.html','wb')
fh.write(data)
fh.close()