user: (genera acquisit e vendite)
	- buy() -> acquisti
	- sell(int) -> vendita
		serial_number
	I. 	avvia 10 thread
	II. 	genera serial_number in modo casuale tra 0 100

productManager: server grpc
	- sell():
		inserisce nella coda laptop_queue
		ritorna "ack"
	- buy():
		consuma dalla coda
		ritorna id 	
	NB. usa lista per la coda dim = 5
		Prima di ritorna inviano una richiesta post 
			{
				"operation": "",
				"serial_number": 10
			}
HistoryServer:
	- POST
		I. Scrive in append sul file history.txt
