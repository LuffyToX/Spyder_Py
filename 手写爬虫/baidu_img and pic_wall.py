# 从 image.baidu.com 爬取图片以及形成照片墙

# 爬取图片
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


# 生成照片墙
import PIL.Image as Image
import os
import math
class My_pho_wall:
    def __init__(self, path, key):
        self.path = path
        self.key_word = key
        self.width = 0
        self.height = 0


    # 设置单个照片的大小
    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size)


    # 获取照片
    def get_pic(self):
        pic_list = os.listdir(self.path)
        pic_list.sort()
        pic_num = len(pic_list)
        pic_row_num = int(math.sqrt(pic_num))
        if pic_num%pic_row_num == 0:
            pic_col_num = pic_num // pic_row_num
        else:
            pic_col_num = pic_num // pic_row_num + 1

        print('I got %d pictures and %d pictures in one row, %d pictures in one column.'%(pic_num, pic_row_num, pic_col_num))
        return pic_list, pic_row_num, pic_col_num


    def compose_pic(self):
        pic_list, pic_row_num, pic_col_num = self.get_pic()
        # 新建一块画布，图片见间隔为 10
        canvas = Image.new('RGB', (self.width*pic_row_num+10*(pic_row_num-1), self.height*pic_col_num+10*(pic_col_num-1)))
        x = 0
        y = 0
        for i in pic_list:
            try:
                path_i = self.path + '\\' + i
                img = Image.open(path_i)  # 打开图片
            except IOError:
                print("Error: 没有找到文件或读取文件失败", i)
            else:
                img = img.resize((self.width, self.height), Image.ANTIALIAS)  # 缩小图片
                canvas.paste(img, (x*(self.width+10), y*(self.height+10)))  # 拼接图片
                x += 1
            if x == pic_row_num:
                x = 0
                y += 1
        # 保存图片
        os.getcwd()
        canvas.save(self.key_word + ".jpg")


if __name__ == "__main__":
    path = "C:\\Users\\Dell\\Desktop\\PHM"
    key = "庞慧敏"
    my_pic = My_baidu_pic(key, path)
    my_pic.download_pic()

    my_pho_wall = My_pho_wall(path, key)
    my_pho_wall.size = 256, 325
    my_pho_wall.compose_pic()


