# POST表单测试网页：http://www.iqianyue.com/mypost/

import urllib.request
import urllib.parse

url = r'http://www.iqianyue.com/mypost/'

# 网页中右键——>网页源代码
# 找到对应的 form 表单部分
'''
<body>
<form action="" method="post">
name:<input name="name" type="text" /><br>
passwd:<input name="pass" type="text" /><br>
<input name="" type="submit" value="submit" />
'''
# 字段名分别为 'name', 'pass'
# {字段名1:字段值1, 字段名2:字段值2,...}
message = {
    "name":'ceo@iqianyue.com',
    "pass":'aA123456'
}

# 将表单数据用 urlencode 编码处理后，再用 encode 设置为 utf-8 编码
postdata = urllib.parse.urlencode(message).encode('utf-8')

# 创建 Request 对象，参数包括URL地址和要传递的数据
# req = urllib.request.Request(url地址, 传递的数据)
req = urllib.request.Request(url, postdata)

# 添加头信息，模拟浏览器爬行
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")

data = urllib.request.urlopen(req).read()

fhandle = open(r'C:\Users\Dell\Desktop\Program\learn_python\learn_spider\spider_base\09.html','wb')
fhandle.write(data)
fhandle.close()


