import urllib.request

for i in range(1, 100):
    try:
        # 设置超时时间为 1s（timeout=1）
        file = urllib.request.urlopen(r"http://www.baidu.com", timeout=1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常 ——>" + str(e))