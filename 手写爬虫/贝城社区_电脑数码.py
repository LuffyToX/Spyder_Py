# -*- coding: utf-8 -*-

""" 贝城社区电脑数码下网页爬取 """

import re
import urllib.request

class Ibeike:
    def __init__(self, url, page):
        self.url = url
        self.page = page

    def get_url(self):
        """ 获取网页 """
        # 模拟成浏览器
        headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3708.400 QQBrowser/10.4.3661.400")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]

        # 将 opener 安装为全局
        urllib.request.install_opener(opener)

        # 打开并读取网页源代码
        self.url = self.url + str(self.page) + '.html'
        data = str(urllib.request.urlopen(self.url).read())

        return data


    def getlink_tiezi(self):
        """ 获取所有帖子链接 """
        data = self.get_url()

        # 构造帖子的正则表达式
        pat = re.compile('thread-\d*-1-' + str(self.page) + '\.html')
        link_list = list(set(pat.findall(data)))

        url_list = []
        for link in link_list:
            url = 'http://city.ibeike.com/' + link
            url_list.append(url)

        return url_list


    def get_link_daohang(self):
        """ 获取导航的所有链接 """
        data = self.get_url()

        # 构造板块导航的正则表达式（每一页的板块导航链接相同）
        pat = re.compile('forum-\d*-1\.html')
        link_list = list(set(pat.findall(data)))

        url_list = []
        for link in link_list:
            url = 'http://city.ibeike.com/' + link
            url_list.append(url)

        return url_list


if __name__ == "__main__":
    url = 'http://city.ibeike.com/forum-281-'

    Page = int(input("Give me a page: "))

    tiezi_link_list = []
    for page in range(1, Page):
        ibeike = Ibeike(url, page)
        tiezi_link_list_page = ibeike.getlink_tiezi()

        tiezi_link_list.append(tiezi_link_list_page)
    #print(tiezi_link_list)

    daohang_link_list = Ibeike(url, 1).get_link_daohang()
    #print(len(daohang_link_list))
    #print(daohang_link_list)

    print("**** 正在爬取帖子网页 ****")
    x = 1
    y = 1
    for url_page in tiezi_link_list:
        for url in url_page:
            path = 'C:\\Users\\hetao\\Desktop\\贝城社区_电脑数码\\帖子\\' + str(x) + '_' + str(y) + '.html'
            fh = urllib.request.urlretrieve(url, filename=path)
            urllib.request.urlcleanup()
            print("**** 第 %d 页的第 %d 个网页爬取完毕 ****" % (x, y))
            y = y + 1
        y = 1
        x = x + 1

    print("**** 正在爬取板块导航网页 ****")
    z = 1
    for url in daohang_link_list:
        path = 'C:\\Users\\hetao\\Desktop\\贝城社区_电脑数码\\板块导航\\' + str(z) + '.html'
        fh = urllib.request.urlretrieve(url, filename=path)
        urllib.request.urlcleanup()
        print("**** 第 %d 个网页爬取完毕 ****" %z)
        z = z + 1