from socket import *
import threading
import time

RECEIVER_TO_PORT = 7000
BUFFER_SIZE = 1024


def do_client(sock, name):
    buf = s.recv(BUFFER_SIZE)
    encoding = 'utf-8'
    strout = str(buf, encoding)
    print(name + strout)


s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', RECEIVER_TO_PORT))     # (ip, port)

cnt = 1

while True:
    x = threading.Thread(target=do_client(s, str(cnt)), args=(1,))
    cnt = cnt + 1
    x.start()


