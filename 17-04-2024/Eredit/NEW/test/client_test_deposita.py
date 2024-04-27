import socket
import sys

try:
    host = sys.argv[1].split(':')[0]
    port = int(sys.argv[1].split(':')[1])
except:
    print("err")
    sys.exit(-1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', port))

print("connesso")

msg = '-'.join(['deposita-smartphone-10']).encode('utf-8')

# msg = '-'.join(['preleva-smartphone']).encode('utf-8')

s.send(msg)

response = s.recv(1024).decode('utf-8')

print(response)


