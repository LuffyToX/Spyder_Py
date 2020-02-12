# 爬取京东手机分类页面图片
import re
import urllib.request
import urllib.error

def craw(url, page):
    # 读取对应网页的全部源代码
    html1 = str(urllib.request.urlopen(url).read())
    # 用于第一次过滤的正则表达式
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    #print(result1)

    # 用于第二次过滤的正则表达式，提取该网页上所有目标图片的链接
    pat2 = '<img width="220" height="220" data-img="1" src="(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    #print(imagelist)

    x = 1
    for imageurl in imagelist:
        imagename = "C:\\Users\\Dell\\Desktop\\Program\\learn_python\\crawl\\jd_phone\\"+'Page'+str(page)+' '+str(x)+".jpg"
        imageurl = "http:"+imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
        x += 1

for i in range(1, 3):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url, i)