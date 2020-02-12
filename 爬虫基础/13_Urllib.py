import urllib.request
import urllib.error

try:
    urllib.request.urlopen(r"http://blog.bussinessss.net")
except urllib.error.URLError as e:
    #print(e.code)   # 远程URL不存在，没有 code
    print(e.reason)