# 套接字 - 基于 UDP 协议 Echo 服务器

from socket import *
from time import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('localhost', 6789))
while True:
    data, addr = server.recvfrom(1024)
    server.sendto(data, addr)
server.close()