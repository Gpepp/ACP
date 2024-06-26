# Definizione
Sono un meccanismo di comunicazione basato su rete.
Quelle che interessano a noi sono:
- [[#TCP]]
- [[#UDP]]
Le socket sono caratterizzate da _Indirizzo IP_, *Numero di porto*. ![[Screenshot 2024-04-24 alle 11.16.43.png]]

# Python

## Configurazione
Modulo **socket** 

```python
import socket
s = socket.socket(socket_family, socket_type)
```

- socket_family: rappresenta la tipologia di indirizzo (ipv4 o ipv6)
	- `socket.AF_INET`  ipv4
- socket_type: rappresente la tipologia di socket
	- `socket.SOCK_STREAM` TCP
	- `socket.SOCK_DGRAM` UDP
### Funzioni delle socket
- `socket()`: crea una nuova socket
- `bind(address)`: binding della socket dove address è una tupla `address = (ip, port)`
- `listen(backlog)`: si mette in ascolto di connessioni (solo in **TCP**)
- `accept()`: segue bind e listen e restituisce `conn, addr = accept()` 
	- `conn` : nuova socket utilizzabile per spedire e ricevere i dati
	- `addr`: indirizzo associato alla socket all'altro capo della connessione
- `connect(address)`: apre una connessione veerso l'indirizzo `address= (ip,port)`
- `close()`: chiude la socket
### Scambio dati
#### TCP
- `send(string)` invia dati tramite socket
- `recv(bufsize)`: riceve i dati tramite socket
##### Server
```python
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = (localhost, 0)
s.bind(address) #con 0 il computer stabilsce in automatico la port
my_sock = s.getsockname() # restituisce ip e port
conn, addr = accept()
data = conn.recv(1024)
conn.send(msg.encode("utf-8"))
conn.close()
s.close()
```
##### Client
```python
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = (localhost, 55555) # porta ricevuta da server
s.send(msg.encode("utf-8"))
data = s.recv(1024).decode("utf-8")
s.close()
```

#### UDP
- `sendto(string, address)` invia dati tramite socket
	- la socket non deve essere connessa dato che l'indirizzo lo specifico con address
- `recvfrom(bufsize)`: riceve i dati tramite socket
	- il valore di ritonro è `string, address`
##### Server
```python
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = (localhost, 0)
s.bind(address) #con 0 il computer stabilsce in automatico la port
my_sock = s.getsockname() # restituisce ip e port
data, addr = s.recvfrom(1024) # 1024 rappresenta il buffsize
s.sendto(msg.encode("utf-8"), addr)
s.close()
```
##### Client
```python
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address = (localhost, 55555) # porta ricevuta da server
s.sendto(msg.encode("utf-8"), address)
data, addr = s.recvfrom(1024).decode("utf-8")
s.close()
```
## Configurazione Multi-thread Multi-process
I thread/Process devono prevedere un costruttore la `run_fun`che contiene il codice sorgente
- TCP: ogni connessione é gestita da un thread/processo differente
- UDP: ogni richiesta é gestita da un thread/processo differente
```python
import threading

def thd_fun(c):
	data = c.recv(1024)
	data = #fa quello che deve
	c.send(data.encode('utf-8'))
	c.close()

if __name__=='__main__':
	s = socket.socket(socket.AF_INET, socket.SOCKT_STREAM)
	s.bind((host,port))
	s.listen(5)
	while True:
		c, addr = s.accept()
		t = threadind.Thread(target=thd_fun, args=(c,)) #args vuoel una tupla
		t.start()
	s.close()
	
```

```python
import multiprocess as mp

def proc_fun(c):
	data = c.recv(1024)
	data = #fa quello che deve
	c.send(data.encode('utf-8'))
	c.close()

if __name__=='__main__':
	s = socket.socket(socket.AF_INET, socket.SOCKT_STREAM)
	s.bind((host,port))
	s.listen(5)
	while True:
		c, addr = s.accept()
		p = mp.Process(target=proc_fun, args=(c,)) #args vuoel una tupla
		p.start()
	s.close()
	
```