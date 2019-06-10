import urllib.parse
import urllib.request

url = 'http://wx4.sinaimg.cn/large/006tkBCzly1fy8hfqdoy6j30dw0dw759.jpg'

with urllib.request.urlopen(url) as response:
    data = response.read()
    f_name = 'download.jpg'
    with open(f_name, 'wb') as f:
        f.write(data)
        print('download successed!')