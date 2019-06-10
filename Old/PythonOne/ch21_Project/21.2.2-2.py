import urllib.request
import ssl

# 为了忽略 SSL 证书验证
context = ssl._create_unverified_context()

url = 'https://q.stock.sohu.com/hisHq?code=cn_600519&stat=1&order=d&callback=historySearchHandler&rt=jsonp&0.8115656498417958'
req = urllib.request.Request(url)

with urllib.request.urlopen(req, context=context) as response:
    data = response.read()
    htmlstr = data.decode('gbk')
    print('htmlstr:',htmlstr)
    htmlstr = htmlstr.replace('historySearchHandler(','')
    htmlstr = htmlstr.replace(')','')
    print('替换后的：',htmlstr)