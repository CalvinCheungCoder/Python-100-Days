from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('172.16.7.67',6789))
    server.listen(512)
    print('服务器启动监听')
    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        client.send(str(datetime.now().encode('utf-8')))
        client.close()

if __name__ == '__main__':
    main()