# -*- coding: utf-8 -*- 
# 
print ' best http://www.jms58.com '
import re
import urllib

def Rurl(url):
    url=urllib.urlopen(url)
    page=url.read()
    return page

def novel(page):
    d1=re.compile(r'<P>(.*)</P>')
    dd1=re.findall(d1,page)
    dd1=''.join(dd1)

    #d2=re.compile(r'&nbsp;')
    ddd=dd1.replace('&nbsp;',' ')

    #dd2=d2.sub(ddd,dd1)
    #d3=re.compile(r'<br />')
    dd3=ddd.replace('<br />','\n')

    return dd3

def Curl(url,num):
    a=url.split('/')
    b=a[-1].split('.')
    c=int(b[0])+num
    a[-1]=str(c)+'.'+b[1]
    e=a[0]+'/'
    for i in range(1,len(a)-1):
        e+=a[i]+'/'
    e=e+a[-1]
    return e

def Csave(dd3):
    read=file('novle.txt','a+')
    read.write(dd3)
    read.close()
    
url=raw_input('site url:')
num=int(raw_input('chapter:'))
for i in range(0,int(num)):
    url1=Curl(url,int(i))
    page=Rurl(url1)
    dd3 = novel(page)
    Csave(dd3)
    print  i




