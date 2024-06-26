import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost',0))
print(f"Port: {s.getsockname()[1]}")

s.listen(10)

while True:
    conn, add = s.accept()
    resp = conn.recv(1024)
    print(f"Messaggio: {resp.decode('utf-8')}")
    