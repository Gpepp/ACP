Client (StompActiveMQ) - Genera 10 req deposita; 5 preleva; 1 svuota:
	- Invia N messaggi sulla coda Richiesta:
		I. 	tipo_richiesta (deposita, preleva, svuota)
		II.	id_articolo (int)
		III.	prodotto (laptop, smartphone)
	- Si mette in ascolto su una coda Risposta

Dispatcher: 
	- Preleva le richiesta da coda Richiesta e le inoltra al server
	- Invoca un nuovo processo per con il metodo corrispondente

Server (gRPC server/Dispathcer):
	- Implemeta i metodi
		I. 	preleva
		II.	deposita
		III.	svuota
	NB. Acesso alla coda di tipo Prod/Cons
