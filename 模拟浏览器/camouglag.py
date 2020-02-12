# 伪装成浏览器，通过 Fiddler 监控会话信息
import urllib.request
import http.cookiejar

url = 'http://news.163.com/16/0825/09/BVA8A9U500014SEH.html'
# 以字典的形式设置 headers
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.9",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
           "Connection": "keep-alive"}
# 设置 cookie
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http':"127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))

# 建立空列表，为了以指定格式存储头信息
headall = list()

# 通过 for 循环遍历字典，构造出指定格式的 headers 信息
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
# 将指定格式的 headers 信息添加好
opener.addheaders = headall
# 将 opener 安装为全局
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url).read()

fh = open(r"C:\Users\Dell\Desktop\Program\learn_python\learn_spider\browser_camouflag\2.html", "wb")
fh.write(data)
fh.close()

