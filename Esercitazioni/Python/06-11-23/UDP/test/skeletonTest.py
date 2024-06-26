import socket, sys

port = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address = ('127.0.0.1', int(port))

msg = "/user/file_1.doc-bw"

s.sendto(msg.encode('utf-8'), address)


msg, _ = s.recvfrom(1024)

print("msg",msg.decode('utf-8'))