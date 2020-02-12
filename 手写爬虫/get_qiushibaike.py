# 爬取糗事百科
import re
import urllib.request

def getcontent(url, page):
    # 模拟成浏览器
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    # 将 opener 安装为全局
    urllib.request.install_opener(opener)

    # 打开并读取网页源代码
    data = urllib.request.urlopen(url).read().decode('utf-8')

    # 构建对应用户提取的正则表达式
    userpat = '<h2>*(.*?)</h2>'

    # 构建段子内容提取的正则表达式
    contentpat = '<div class="content">(.*?)</div>'

    # 寻找出所有用户
    userlist = re.compile(userpat, re.S).findall(data)
    print(userlist)

    # 寻找出所有内容
    contentlist = re.compile(contentpat, re.S).findall(data)
    print(contentlist)

    x = 1
    # 通过 for 循环遍历段子内容并将内容分别赋给对应的变量
    for content in contentlist:
        content = content.replace("\n", "") # 替换换行符
        content = content.replace("<span>", "")
        content = content.replace("<br/>", "。")
        # 用字符串作为变量名，先将对应字符串赋给一个变量
        name = "content"+str(x)
        # 通过 exec() 函数实现用字符串作为变量名并赋值
        exec(name+'=content')
        x += 1

    y = 1
    # 通过 for 循环遍历用户，并输出该用户对应的内容
    for user in userlist:
        name = "content"+str(y)
        print("用户"+str(page)+str(y)+"是："+user)
        print("内容是：")
        exec("print("+name+")")
        print("\n")
        y += 1

# 分别获取各页的段子
for i in range(1, 3):
    url = "https://www.qiushibaike.com/text/page/"+str(i)
    getcontent(url, i)