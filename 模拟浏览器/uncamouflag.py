# 没有设置浏览器伪装，通过 Fiddler 监控会话信息
import urllib.request
import http.cookiejar

url = 'http://news.163.com/16/0825/09/BVA8A9U500014SEH.html'
cjar = http.cookiejar.CookieJar()

proxy = urllib.request.ProxyHandler({'http':"127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()

fh = open(r"C:\Users\Dell\Desktop\Program\learn_python\learn_spider\browser_camouflag\1.html", "wb")
fh.write(data)
fh.close()