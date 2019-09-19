from json import *
import urllib.request
import json
import ssl
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()

f = open("/Users/zhangdinghao/Desktop/1.txt")
for line in f.readlines():                          #依次读取每行
    line = line.strip()                             #去掉每行头尾空白
    if not len(line) or line.startswith('#'):       #判断是否是空行或注释行
        continue                                    #是的话，跳过不处理
    dict = eval(line)

    url = dict['href']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req,context=context)
    html = res.read().decode('utf-8')

    soup = BeautifulSoup(html,'html.parser')

    articleTitle = ''
    timeString = ''
    contentString = ''
    arr = []

    for title in soup.find_all('header'):

        for titleTwo in title.find_all('h1'):
            titleStr = titleTwo.find_all('a')[0]
            articleTitle = titleStr.string

        for time in title.find_all('ul'):
            timeTwo = time.find_all('li')[0]
            timeString = timeTwo.string

    for content in soup.find_all('article'):
        for contentStr in content.find_all('div'):
            print(contentStr.string)

    print(articleTitle)
    print(timeString)
    print(arr)

    break
    # for title in soup.find_all('header'):


