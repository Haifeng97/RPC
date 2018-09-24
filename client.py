#client
#先运行server，后运行这个
import socket

s = socket.socket()
host = 'localhost'
port = 65530
s.connect((host, port))
while True:
    data = input("Input:")
    if len(data) == 0: continue
    s.sendall(bytes(data, encoding='gbk'))
    server_reply = s.recv(1024)
    print('Reply:' + str(server_reply, encoding="gbk"))