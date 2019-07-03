# 套接字 - 基于 TCP 协议创建时间服务器

from socket import *
from  time import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost',6789))
server.listen()

print('服务器已经启动正在监听客户端连接')
while True:
    client, addr = server.accept()
    print('客户端 %s:%d 连接成功' % (addr[0], addr[1]))
    currtime = localtime(time())
    timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
    client.send(timestr.encode('utf-8'))
    client.close()
server.close()