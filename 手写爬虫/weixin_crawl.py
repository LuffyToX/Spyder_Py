import re
import time
import urllib.request
import urllib.error

# 模拟浏览器
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400")
opener = urllib.request.build_opener()
opener.addheaders = [headers]

# 将 opener 安装为全局
urllib.request.install_opener(opener)

# 设置一个列表存储文章网址
listurl = list()

# 使用代理服务器
def use_proxy(proxy_addr, url):
    # 建立异常处理机制
    try:
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        # 若为 URLError 异常，延时 10s 执行
        time.sleep(10)
    except Exception as e:
        print("Exception:"+str(e))
        # 若为 Exception 异常，延时 1s 执行
        time.sleep(1)

# 获取所有文章链接
def getlisturl(key, pagestart, pageend, proxy):
    try:
        page = pagestart

        # 编码关键字 key
        keycode = urllib.request.quote(key)
        # 编码 "&page"
        pagecode = urllib.request.quote("&page")

        # 循环爬取各页的文章链接
        for page in range(pagestart, pageend+1):
            # 分别构建各页的 url 链接，每次循环构建一次
            url = "http://weixin.sogou.com/weixin?type=2&query="+keycode+pagecode+str(page)

            # 用代理服务器爬取，解决 IP 被封杀问题
            data1 = use_proxy(proxy, url)

            # 获取文章链接的正则表达式
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            # 获取每页的文章链接并添加到列表中
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
        print("共获取到"+str(len(listurl))+"页") # 便于测试
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        # 若为 URLError 异常，延时 10s 执行
        time.sleep(10)
    except Exception as e:
        print("Exception:"+str(e))
        # 若为 Exception 异常，延时 1s 执行
        time.sleep(1)

# 通过文章链接获取对应内容
def getcontent(listurl, proxy):
    i = 0
    # 设置本地文件中的开始 html 编码
    html1 = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://
    www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>微信文章页面</title>
</head>
<body>'''
    fh = open(r"C:\Users\Dell\Desktop\Program\learn_python\learn_spider\weixin.html", "wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    # 以追加写入的方式打开文件，以写入对应文章内容
    fh = open(r"C:\Users\Dell\Desktop\Program\learn_python\learn_spider\weixin.html", "ab")
    # 此时 listurl 为二维列表，形如：listurl[][]，
    # 第一维存储的信息跟第几页相关，第二维存储的信息跟该页第几个文章链接相关
    for i in range(0, len(listurl)):
        for j in range(0, len(listurl[i])):
            try:
                url = listurl[i][j]
                # 处理成真实 url（采集网址比真实网址多了一串amp）
                url = url.replace("amp;", "")
                # 使用代理去爬取对应网址的内容
                data = use_proxy(proxy, url)
                # 文章标题正则表达式
                titlepat = '<title>(.*?)</title>'
                # 文章内容的正则表达式
                contentpat = 'id="js_content">(.*?)id="js_sg_bar">'
                # 通过对应正则表达式找到标题并赋给列表 title
                title = re.compile(titlepat).findall(data)
                # 通过对应正则表达式找到标题并赋给列表 content
                content = re.compile(contentpat,re.S).findall(data)

                # 初始化标题与内容
                thistitle = "此次没有获取到"
                thiscontent = "此次没有获取到"

                # 如果表土列表不为空，说明找到了标题，去列表第0个元素，即此次标题赋给变量thistitle
                if title != []:
                    thistitle = title[0]
                if content != []:
                    thiscontent = content[0]
                # 将标题与内容汇总赋给变量 dataall
                dataall = "<p>标题为："+thistitle+"</p><p>内容为："+thiscontent+"</p><br>"
                # 将该篇文章的标题与内容的总信息写入对应文件
                fh.write(dataall.encode("utf-8"))
                print("第"+str(i)+"个网页第"+str(j)+"次处理") # 便于测试
            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    e.code
                if hasattr(e, "reason"):
                    e.reason
                # 若为 URLError 异常，延时 10s 执行
                time.sleep(10)
            except Exception as e:
                print("Exception: "+str(e))
                # 若为 Exception 异常，延时 1s 执行
                time.sleep(1)
    fh.close()
    # 设置并写入本地文件的 html 后面结束部分代码
    html2 = '''</body>
</html>
    '''
    fh = open(r"C:\Users\Dell\Desktop\Program\learn_python\learn_spider\weixin.html", "ab")
    fh.write(html2.encode("utf-8"))
    fh.close()

# 设置关键词
key = "物联网"
# 设置代理服务器
proxy = "117.131.99.210:53281"
# 起始页
pagestart = 1
#结束页
pageend = 2
listurl = getlisturl(key, pagestart, pageend, proxy)
getcontent(listurl, proxy)

