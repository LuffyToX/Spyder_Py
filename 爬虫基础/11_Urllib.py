import urllib.request

httphd = urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPSHandler(debuglevel=1)

# 创建自定义的 opener 对象
opener = urllib.request.build_opener(httphd, httpshd)
# 创建全局默认的 opener 对象
urllib.request.install_opener(opener)

url = "http://edu.51cto.com"
data = urllib.request.urlopen(url)