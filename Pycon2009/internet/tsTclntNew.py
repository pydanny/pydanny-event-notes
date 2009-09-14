from socket import *

HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:

    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    print '...waiting for reply...'
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data
    
tcpCliSock.close()