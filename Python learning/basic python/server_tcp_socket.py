import socket
import threading
import time
def tcplink(sock,addr):
    print("accept new connection from %s:%s..." %addr)
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello,%s' %data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' %addr)

fd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
fd.bind(('127.0.0.1',8888))
fd.listen(5)
print('waiting for connection...')
while True:
    sock,addr = fd.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()


