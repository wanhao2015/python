import socket

fd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
fd.bind(('127.0.0.1',8888))
print("Bind Udp on 8888...")
while True:
    data,addr = fd.recvfrom(1024)
    # data = str(data,encoding='utf-8')
    print('Received from %s:%s' %addr)
    fd.sendto(b'hello,%s' %data,addr)
