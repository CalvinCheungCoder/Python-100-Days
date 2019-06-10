import urllib.request
import ssl
import re
from bs4 import BeautifulSoup

# 为了忽略 SSL 证书验证
context = ssl._create_unverified_context()

url = 'http://www.528btc.com/e/action/ListInfo/index.php?page=4&classid=28&totalnum=584'
req = urllib.request.Request(url)

with urllib.request.urlopen(req, context=context) as response:
    data = response.read()
    htmlstr = data.decode()

    soup = BeautifulSoup(htmlstr,"html.parser")
    right = soup.select('i[class="right"]')
    for trtag in right:
        name = trtag.select('a')[0].get_text()
        des = trtag.select('p')[0].get_text()
        intro = trtag.select('p')[1].get_text()
        data = {
            'name': name,
            'des': des,
            'intro':intro
        }
        print(data)
        print(',')
