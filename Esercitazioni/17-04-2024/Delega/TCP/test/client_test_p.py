import socket
import sys


port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', port))
msg = 'preleva-laptop'.encode('utf-8')
s.send(msg)
resp = s.recv(1024)

print(resp.decode('utf-8'))

