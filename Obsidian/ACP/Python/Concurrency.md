Per la programmazione concorrente python mette a disposizione due moduli [[#Threading]] e [[#Multiprocess]]
# Threading

[Threading - docs](https://devdocs.io/python~3.12/library/threading)
[Threading - pydoc ](https://docs.python.org/3/library/threading.html#)
Il modulo mette a disposizione delle calssi:
- Thread [[#Thread]]
- Thread-Lock Data
- Lock/Rlock
- Condition
- Semaphore
- Event

## Thread
### Funzionamento
Implementazione tramite costruttore:
```
def th_fun(c):
	pass

if __name__ =="__main__":
	t = threading.Thread(target=th_fun, args=(a1,))
	t.start()
	t.join()
```
Implementazione tramite classe:
```
class myThread(threading.Thread):
	def run(self):
		pass
		
if __name__ =="__main__":
	t = myThread()
	t.start()
	t.join()
	
```

Alcuni metodi e argomenti
- Thread
	- group: riservato a future implementazioni deve essere `None`
	- target: rappresenta la run function del Thread ('callable object')
	- name: nome del thread
	- args: tupla che contiene gli argomenti da passare alla funzione
	- kwargs: dizionario di keyword da passare alla funzione invocatrice
	- daemon: boleano che indica se demone o meno
	- \*
- start: Avvia il Thread
- run: metodo che contine la funzione del thread
- join(timeout=None): numero di floating
- is_alive(): ritorna se attivo o meno
#### Dati Locali
Per ongi Thread potrebbe essere necessario salvarte alcuni dati locali; allora python mette a disposizione la classe local
`var = threading.local()`
### Gestione della concorrenza
#### Lock
Alla creazione di un lock esso si trova nello stato *unlocked*:
- acquire(): acquisisce il lock quando lo stato è *unlocked* e lo pone a *locked*
- releas(): rilascia il lock dallo stato *locked* a quello *unlocked* 
  **NB: lo puo invocare solo chi ha acquisito il lock**
#### RLock
(reentrant lock) ***Ricordati di farlo***
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
#### Condition


# Multiprocess
