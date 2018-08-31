import socket

# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",8080)
fd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
fd.connect(('www.sina.com.cn',80))
fd.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = fd.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
fd.close()
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
    f.write(html)
