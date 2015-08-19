# -*- coding: utf-8 -*-
import urllib
import re
import time
def page(url):
    html=urllib.urlopen(url)
    page=html.read()
    d=url.split('/')
    com=d[0]+'//'+d[2]
    return page,com


def html(page):
    pp=re.compile(r'href="(.*\.html)')
    al=re.findall(pp,page)
    return al

def getImage(html):
    rew=r'src=\'(.*\.jpg)\''
    imgre=re.compile(rew)
    imagelist=re.findall(imgre,html)
    print imagelist
    for img in imagelist:
        y= time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        urllib.urlretrieve(img,'%s.jpg' % y)

def getHtml(url):
    page=urllib.urlopen(url)
    html = page.read()
    return html

url=raw_input('url:')
page,com=page(url)
al=html(page)
urlA=[]
for i in al:
    urlA.append(com+'/'+i)
for i in range(8,len(urlA)):
    print urlA[i]
    htmlF=getHtml(urlA[i])
    getImage(htmlF)


