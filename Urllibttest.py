import urllib.request
import os
import re
import urllib
import bs4

#py抓取页面图片并保存到本地

#获取页面信息
def getHtml(url):
    headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }
    #req = urllib.request.Request(url, None, headers)
    #buff = urllib.request.urlopen(req).read()
    #html = buff.decode("utf-8")
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    buff = response.read()
    html = buff.decode("utf-8")
    return html


#通过正则获取图片
def getImg(html):
    reg = "https://.+?.+JPEG"
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print(imglist)
    return imglist

html = getHtml("http://www.baidu.com")

imglist = getImg(html)


#循环把图片存到本地
x = 0
for imgurl in imglist:
    print(x)
    urllib.request.urlretrieve(imgurl,'d:/wong/%s.jpg'%x)
    x+=1

print("done")












