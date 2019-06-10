import urllib.request
import ssl

# 为了忽略 SSL 证书验证
context = ssl._create_unverified_context()

url = 'https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'
req = urllib.request.Request(url)

with urllib.request.urlopen(req, context=context) as response:
    data = response.read()
    htmlstr = data.decode()
    print(htmlstr)