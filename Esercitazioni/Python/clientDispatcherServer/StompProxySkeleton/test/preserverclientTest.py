import socket, sys


if __name__ == "__main__":

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(('localhost', 50501))

    message = "preleva-"
    sk.send(message.encode('utf-8'))

    msg = sk.recv(1024).decode('utf-8')
    print(msg)
