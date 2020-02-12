import re
import urllib.request
import urllib.error
class My_baidu_pic:
    def __init__(self, key, file):
        self.key_word = key
        self.file = file


    # 根据关键字得到相应网址
    def get_key_url(self):
        url_begin = \
            "http://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word="
        key_word = urllib.request.quote(self.key_word)
        url = url_begin + key_word
        return url


    # 得到搜索结果中每一张图片的 url
    def get_pic_url(self):
        url = self.get_key_url()

        # 模拟浏览器
        req = urllib.request.Request(url)
        # 添加报头信息
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")

        # 读取对应网页的全部源代码
        html = str(urllib.request.urlopen(req).read())
        # 构建原图下载地址的正则表达式
        # 以 "objURL"开始，以 , 结束
        pat = '"objURL":"(.*?)",'
        result = re.compile(pat, re.S).findall(html)
        #result = result[0]
        #print(result)   # 供测试用
        return result


    # 下载并保存图片到本地
    def download_pic(self):
        imglist = self.get_pic_url()
        #print(imglist)
        x = 1
        for imageurl in imglist:
            imagename = self.file + "\\" + str(x) + ".jpg"
            #print(imageurl)
            try:
                urllib.request.urlretrieve(imageurl, filename=imagename)
            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    x += 1
                if hasattr(e, "reason"):
                    x += 1
            x += 1

if __name__ == "__main__":
    path = "C:\\Users\\Dell\\Desktop\\迷宫"
    key = "scratch游戏背景图"
    my_pic = My_baidu_pic(key, path)
    my_pic.download_pic()