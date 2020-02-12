import urllib.request

key_word = "哈士奇"
key_code = urllib.request.quote(key_word)

url = "http://www.baidu.com/s?wd=" + key_code

req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()

fh = open(r'C:\Users\Dell\Desktop\Program\learn_python\learn_spider\spider_base\08.html','wb')
fh.write(data)
fh.close()