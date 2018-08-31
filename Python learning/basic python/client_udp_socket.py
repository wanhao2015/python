import socket

fd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael',b'Tracy',b'Sarach']:
    fd.sendto(data,('127.0.0.1',8888))
    print(fd.recv(1024).decode('utf-8'))
fd.close()
