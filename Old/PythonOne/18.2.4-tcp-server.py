import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8880))
s.listen()
print('服务器启动。。。')

conn, address = s.accept()
print(address)

data = conn.recv(1024)
print('从客户端收到消息：{0}'.format(data.decode()))
conn.send('123456 hello'.encode())

conn.close()
s.close()