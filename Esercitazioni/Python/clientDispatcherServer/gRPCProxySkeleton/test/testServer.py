import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50501))

msg = "deposita-1"

s.send(msg.encode('utf-8'))

resp = s.recv(1024)

print(f"resp-{resp.decode('utf-8')}")


