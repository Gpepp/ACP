import socket, sys

port = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',int(port)))

#s.send('deposita-10'.encode('utf-8'))
s.send('preleva'.encode('utf-8'))

rsp = s.recv(1024)

print(rsp.decode('utf-8'))