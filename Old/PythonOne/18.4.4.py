import urllib.request
import urllib.parse

url = 'http://wwww.51work6.com/service/mynotes/WebService.php'
params_dict = {'email':'984382258@qq.com', 'type':'JSON', 'action':'query'}
params_str = urllib.parse.urlencode(params_dict)
print(params_str)

url = url + '?' + params_str
print(url)

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)