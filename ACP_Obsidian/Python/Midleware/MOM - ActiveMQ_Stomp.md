
[Riferimenti](https://jasonrbriggs.github.io/stomp.py/api.html)

Usage
```python
import stomp
conn = stomp.Connection([(host,port)]) 
conn.connect()
# Invio e ricezione dei messaggi.
conn.disconnect() # per la disconnessione
```

- Default Port di ActiveMQ: 61613
- Connection()
	Accetta una lista di tuple formate da host e port, in modo da poter effettuare il check delle varie coppie, fin quando una socket connection non viene stabilita con successo
- Connect()
	- *username* $\rightarrow$ username per il login (str)
	- *passcode* $\rightarrow$ passwrod per il login (str)
	- *wait* $\rightarrow$ attende che la connessia sia stabilita (bool)
	- *headers* $\rightarrow$ headers addizionali da inviare (dict)
	- *with_connect_command* $\rightarrow$ 
	- *keyword_headers* $\rightarrow$

### Invio di messaggi
```python
conn.send('queue/test', 'test message')
```


- send()
	- *destination*
	- *body*
	- *content_type*
	- *headers*
	- *keyword_headers*

### Ricezione
```python
conn.set_listener('name', MyListener())
conn.subscribe(destination='queue/test', id=1, ack='auto')
```

- subscribe():
	- destination $\rightarrow$ topic o queue (str)
	- id $\rightarrow$ Identificativo univoco della sottoscrizione (str)
	- ack $\rightarrow$ modalità di acknowledgement ->  auto, client, client-individual(ack,nack)
	- headers
	- keyword_headers
La ricezione avviene attraverso un listener


#### Listener
```python
class MyListener(stomp.ConnectionListener):
	def on_message(self, frame):
		print('recivedmess: ', frame.body)
```



### Example

#### Point-to-Point

```python
#Client
import time, stomp
class MyListener(stomp.ConnectionListener):
	def __init__(self, conn):
		self.conn = conn
		
	def on_message(self, frame):
		print('recivedmess: ', frame.body)

if __name__ == "__main__":
	conn = stomp.Connection([('127.0.0.1', 61613)])
	conn.set_listener('name', MyListener(conn))
	conn.connect(wait=True)
	conn.subscribe(destination='/queue/test', id=1, ack='auto')
	time.sleep(60)
	conn.disconnect()
```



```python
#Sender
import stomp
conn = stomp.Connection([('127.0.0.1', 61613)])
conn.connect(wait=True)
conn.send('queue/test', 'test message')
conn.disconnect()
```

#### pub-sub

```python
# Subscriber
import time, stomp
class MyListener(stomp.ConnectionListener):
	def __init__(self, conn):
		self.conn = conn
		
	def on_message(self, frame):
		print('recivedmess: ', frame.body)

if __name__ == "__main__":
	conn = stomp.Connection([('127.0.0.1', 61613)])
	conn.set_listener('name', MyListener(conn))
	conn.connect(wait=True)
	conn.subscribe(destination='/queue/test', id=1, ack='auto')
	time.sleep(60)
	conn.disconnect()
```

```python
#Sender
import stomp
conn = stomp.Connection([('127.0.0.1', 61613)])
conn.connect(wait=True)
conn.send('topic/test', 'test message')
conn.disconnect()
```

#### transazioni

- I messaggi delle transazioni vengono mantenuti dal server finché non viene effettuato 

```python
#commit

conn.subscribe('queue/test', id=5)
txid = conn.begin()
conn.send('queue/test', 'test1', transaction=txid)
conn.send('queue/test', 'test2', transaction=txid)
conn.send('queue/test', 'test3', transaction=txid)
conn.commit(txid)

#Abort

conn.subscribe('queue/test', id=6)
txid = conn.begin()
conn.send('queue/test', 'test4', transaction=txid)
conn.send('queue/test', 'test5', transaction=txid)
conn.abort(txid)

```