# 项目实战，抓取纳斯达克股票数据

import urllib.request
import hashlib
from bs4 import BeautifulSoup
import os

url = 'https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'

def validateUpdate(html):
    md5obj = hashlib.md5()
    md5obj.update(html.encode(encoding='utf-8'))
    md5code = md5obj.hexdigest()
    print(md5code)

    old_md5code = ''
    f_name = 'md5.txt'

    if os.path.exists(f_name):
        with open(f_name, 'r', encoding='utf-8') as f:
            old_md5code = f.read()

    if md5code == old_md5code:
        print('数据没有更新')
        return False
    else:
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        print('数据更新')
        return True


req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    html = data.decode()

    sp = BeautifulSoup(html, 'html.parser')

    div = sp.select('div#quotes_content_left_pnlAJAX')
    divstring = div[0]

    if validateUpdate(divstring):
        trlst = sp.select('div#quotes_content_left_pnlAJAX table tbody tr')

        data = []
        for tr in trlst:
            trtext = tr.text.strip('\n\r')
            if trtext == '':
                continue

            rows = re.sp