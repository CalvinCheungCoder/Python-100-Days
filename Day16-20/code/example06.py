'''
编码和解码 - BASE64
0-9A-Za-z+/
1100 0101 1001 0011 0111 0110
00110001 00011001 00001101 00110110
base64
b64encode / b64decode
-------------------------------------
序列化和反序列化
序列化 - 将对象变成字节序列(bytes)或者字符序列(str) - 串行化/腌咸菜
反序列化 - 把字节序列或者字符序列还原成对象
Python标准库对序列化的支持：
json - 字符形式的序列化
pickle - 字节形式的序列化
dumps / loads
'''

import base64
import json
import redis

from example02 import Person

class PersonJsonEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

def main():
    cli = redis.StrictRedis(host='120.77.222.217', port=6379, password='123123')
    data = base64.b64decode(cli.get('guido'))
    with open('gudio2.jpg', 'wb') as file_stream:
        file_stream.write(data)

if __name__ == '__main__':
    main()