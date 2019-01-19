import urllib.request

with urllib.request.urlopen('http://www.baidu.com/') as response:
    data = response.read()
    html = data.decode()
    print(html)