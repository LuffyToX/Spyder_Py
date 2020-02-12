import urllib.request
import urllib.error

try:
    urllib.request.urlopen(r"http://www.blog.csdn.net")
except urllib.error.URLError as e:
    print(e.code)   # 异常状态码
    print(e.reason)   # 异常原因