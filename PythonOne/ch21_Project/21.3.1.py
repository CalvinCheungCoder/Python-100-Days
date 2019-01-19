import urllib.request

import os
import re

url = 'http://p.weather.com.cn/'

def findallimageurl(htmlstr):
    pattern = r'http://\S+(?:\.png|\.jpg)'
    return re.findall(pattern, htmlstr)


def getfilename(urlstr):
    pos = urlstr.rfind('/')
    return urlstr[pos + 1:]


url_list = []
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()

    url_list = findallimageurl(htmlstr)

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