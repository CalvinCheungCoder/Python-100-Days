import urllib.request
import json
import ssl
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()

for num in range(1,40):
    url = 'https://www.ym2.net/tag/manzuyongshi/page/' + str(num)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req,context=context)
    html = res.read().decode('utf-8')

    soup = BeautifulSoup(html,'html.parser')
    for tags in soup.find_all('a',target="_blank",):
        title = tags.attrs
        titleString = title.get('title')
        if str(titleString).find('鹰盲') != -1:
            print(title)