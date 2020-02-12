import urllib.request

file = urllib.request.urlopen(r"http://www.baidu.com")

# 返回与当前环境有关的信息
# 爬取的网页.info()
print(file.info())

# 返回当前爬取网页的状态码。若返回200为正确，返回其他则不正确。
# 爬取的网页.getcode()
print(file.getcode())

# 获取当前所爬取的URL地址
# 爬取的网页.geturl()
print(file.geturl())

# 如果在URL中使用一些其他不符合标准的字符就会出问题，此时需要进行URL编码。
# 如果要进行了编码，可以使用 urllib.request.quote()
url_q = urllib.request.quote(r"http://www.sina.com.cn")
print(url_q)

# 解码
url_u = urllib.request.unquote(url_q)
print(url_u)


