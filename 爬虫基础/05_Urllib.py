import urllib.request

url = r'https://www.jianshu.com/p/a6549fd7c951'

# 创建 Resquest对象
req = urllib.request.Request(url)

# 添加报头信息
# Request对象名.add_header(字段名，字段值)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")

# 打开 Request 对象即可打开对应的网址
data = urllib.request.urlopen(req).read()

fhandle = open(r'C:\Users\Dell\Desktop\Program\learn_python\learn_spider\spider_base\05.html', 'wb')
fhandle.write(data)
fhandle.close()