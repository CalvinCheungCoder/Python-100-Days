import os
import urllib.request

from bs4 import BeautifulSoup

url = 'http://p.weather.com.cn/'

def findallimageurl(htmlstr):
    sp = BeautifulSoup(htmlstr, 'html.parser')
    imagetaglist = sp.find_all('img')

    srclist = list(map(lambda u: u.get('src'),imagetaglist))
    filtered_srclist = filter(lambda u: u.lower().endswith('.png') or u.lower().endswith('.jpg'),srclist)
    return filtered_srclist


def getfilename(urlstr):
    pos = urlstr.rfind('/')
    return  urlstr[pos + 1:]

url_list = []
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()

    url_list = findallimageurl(json_data)

for imagesrc in url_list:
    req = urllib.request.Request(imagesrc)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        if len(data) < 1024 * 100:
            continue

        if not os.path.exists('download'):
            os.mkdir('download')

        filename = getfilename(imagesrc)
        filename = 'download/' + filename
        with open(filename, 'wb') as f:
            f.write(data)

    print('下载图片', filename)
