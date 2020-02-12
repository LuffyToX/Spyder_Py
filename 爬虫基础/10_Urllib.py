# 使用代理服务器来爬取某个URL网页
def use_proxy(proxy_addr, url):
    import urllib.request

    # 设置对应的代理服务器信息
    # urllib.request.ProxyHandler({'http':代理服务器地址})
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})

    # 创建 build_opener 对象
    # 第一个参数：代理信息
    # 第二个参数：urllib.request.HTTPHandler 类
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)

    # 创建全局默认的 build_opener 对象，
    # 那么在使用 urlopen 时亦会使用我们安装的 build_opener 对象
    urllib.request.install_opener(opener)

    data = urllib.request.urlopen(url).read().decode('utf-8')

    return data

# 网址:端口号
proxy_addr = "117.131.99.210:53281"
url = "http://www.baidu.com"
data = use_proxy(proxy_addr, url)
print(len(data))

fh = open(r'C:\Users\Dell\Desktop\Program\learn_python\learn_spider\spider_base\10.html','wb')
fh.write(data.encode())
fh.close()

