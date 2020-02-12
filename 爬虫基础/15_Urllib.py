import urllib.request
import urllib.error

try:
    urllib.request.urlopen(r"http://blog.businessss.net")
except urllib.error.URLError as e:
    if hasattr(e, "code"):   # 使用 hasattr()函数判断是否有"code"属性
        print(e.code)
    if hasattr(e, "reason"): # 使用 hasattr()函数判断是否有"reason"属性
        print(e.reason)