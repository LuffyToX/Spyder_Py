# -*- coding:utf-8 -*-

import re
import time
import random
import urllib.request
import urllib.error

class Crawl_data:
    """ 爬取数据 （数据来源：证券之星）"""

    def __init__(self, url, max_page):
        self.url = url
        self.page = int(max_page)


    def get_page_url(self):
        """ 获取相应页面的 url """
        url_page = self.url + str(self.page) + '.html'
        #print(self.url)
        #print(url_page)
        return url_page


    def get_page_ori_code(self):
        """ 获取网页源码 """

        ''' 伪装成浏览器 '''
        # 以字典的形式设置 headers
        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                   "Accept-Language": "zh-CN,zh;q=0.9",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                   "Connection": "keep-alive"}
        # 创建 bulid_opener 对象
        opener = urllib.request.build_opener()

        # 建立空列表，为了以指定格式存储头信息
        headall = list()

        # 通过 for 循环遍历字典，构造出指定格式的 headers 信息
        for key, value in headers.items():
            item = (key, value)
            headall.append(item)
        # 将指定格式的 headers 信息添加好
        # 该格式为 opener.addheaders = [("", ""), ("", ""), ("", ""), ...]
        opener.addheaders = headall
        # 将 opener 安装为全局
        urllib.request.install_opener(opener)

        ''' 打开网页 '''
        try:
            # 设置超时时间为 100s
            html = opener.open(self.get_page_url(), timeout=100)
            #print(type(html))
            return html
        except Exception as e:
            print("出现异常 ——>" + str(e))


    def get_shares_data(self):
        """ 获取股票数据 """
        shares_total = list()  # 所有页面的股票数据
        for page in range(self.page):

            ''' 异常检测 '''
            try:
                html = self.get_page_ori_code()
            except urllib.error.URLError as e:
                if hasattr(e, "code") and hasattr(e, "reason"):
                    print("Page {0} has a fault and it's code is: {1}\nThat means: {2}"\
                          .format(page+1, e.code, e.reason))
                elif hasattr(e, "reason"):
                    print("Page %d has a fault and it's reason is: %s"%(page+1, e.reason))
            except urllib.error.HTTPError as e:
                if hasattr(e, "code") and hasattr(e, "reason"):
                    print("Page {0} has a fault and it's code is: {1}\nThat means: {2}"\
                          .format(page+1, e.code, e.reason))
                elif hasattr(e, "reason"):
                    print("Page %d has a fault and it's reason is: %s" % (page+1, e.reason))

            ''' 获取页码 '''
            html = html.read().decode('gbk')
            print('Get page %d sucessfully!'%(page+1))

            # 匹配主体
            pat_body = re.compile('<tbody[\s\S]*</tbody>')
            body = re.findall(pat_body, str(html))

            # 某页的股票数据
            pat_shares = re.compile('>(.*?)<')
            shares_page = re.findall(pat_shares, body[0])

            shares_total.extend(shares_page)
            # 每抓一页随机休眠几秒，防止被服务器中断
            time.sleep(random.randrange(1, 4))

        ''' 删除空白字符 '''
        #print(shares_total)
        shares_total = [x.strip() for x in shares_total if x.strip()!='']
        print(shares_total)
        return shares_total


def align_print(string, distance, alignment='left'):
    """ 中英混搭时对齐输出 """

    # 计算出 string 的 'gbk' 码长度
    length = len(string.encode('gbk'))
    if distance > length:
        space_to_fill = distance - length
    else:
        space_to_fill = 0

    if alignment == 'left':
        string = string + ' ' * space_to_fill

    elif alignment == 'right':
        string = ' ' * space_to_fill + string

    elif alignment == 'center':
        string = ' ' * (distance // 2) + string + ' ' * (distance - distance // 2)

    return string


if __name__ == "__main__":
    url = 'http://quote.stockstar.com/stock/ranklist_a_3_1_' # 该url不能用于直接搜索
    max_page = input("你想爬取前多少页的信息？")
    data = Crawl_data(url, max_page)
    shares = data.get_shares_data() # 获取数据列表

    ''' 尽管我尝试很多方法试图对齐中英混搭输出，但效果都不尽人意，此种方法是输出效果最佳的 '''
    # 这里只打印前 5 列
    print(align_print('代码', 15), align_print('简称', 15),\
          align_print('最新价', 15), align_print('涨跌幅', 15),\
          align_print('涨跌额', 15), align_print('5分钟涨幅', 15))
    for i in range(0, len(shares), 13):
        print(align_print(shares[i], 15), align_print(shares[i+1], 15),\
              align_print(shares[i+2], 15), align_print(shares[i+3], 15),\
              align_print(shares[i+4], 15), align_print(shares[i+5], 15))


