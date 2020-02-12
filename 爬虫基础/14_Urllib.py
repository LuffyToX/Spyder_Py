import urllib.request
import urllib.error

try:
    urllib.request.urlopen(r"http://blog.businessss.net")
except urllib.error.HTTPError as e:   # 先用 HTTPError 子类进行处理
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:   # 再用 URLError 类处理
    print(e.reason)