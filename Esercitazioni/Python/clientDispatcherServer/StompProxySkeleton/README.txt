Code di messaggi Stomp ActiveMQ

port 50501

CLIENT:
- Il Client invia N messaggi sulla coda Richiesta "queue/Richiesta"
	I. 	Tipo richiesta (deposita/preleva)
	II.	id_articolo (int)

- Il Client si mette in ascolto su una coda Risposta "queue/Risposta"
	I.	deposited/id_articolo


DISPATCHER:
- Preleva le richieste dalla coda e le inoltra al server
	I.	Estrae le infromazioni
	II.	Invoca con un nuovo processo i metodi (preleva/deposita) FORNITI DAL SERVER (PROXY/Skeleton)

SERVER (MultiProcesso):
- Fornisce i metodi Preleva/Deposita
- CODA:
	Dimensio della coda = 5
	Produttore/Consumatore



Note:
- Client Genera 10 messaggi.
- Socket tra Disp e Server TCP
- Pattern Proky/Skeleton per Ereditarietà
