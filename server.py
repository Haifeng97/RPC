#server
#接收字符串，返回大写的
#先运行这个，后运行client
import socket

s = socket.socket()
host = 'localhost'
port = 65530
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()

while True:
    try:
        print('S    erver:' , addr, 'waiting...')
        client_data = conn.recv(1024)
        print("client:", str(client_data, encoding="gbk"))
        send_data = client_data.upper()
        conn.send(send_data)
    except Exception:
        break
conn.close()
