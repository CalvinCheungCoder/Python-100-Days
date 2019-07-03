from time import time
from threading import Thread

import requests

class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/zhangdinghao/Python-100-Days/Day01-15/code/Day14/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=5670b23020bdad387f79cb21b39b4f41&num=10')
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHanlder(url).start()

if __name__ == '__main__':
    main()