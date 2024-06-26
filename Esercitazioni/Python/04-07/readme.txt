Servicer:
	- log (msgLog, tipo)
		I. 	msgLog ( success/checking _tipo 0/1_ o _fatal/exception 2_)
		II. 	tipo (0 = DEBUG,1 = INFO, 2 = ERROR)
LoggingServer:
	- ILogging 
		- log (str,int)
			I.	avvia rpceso produttore
			II.	inserisce nella coda process-safe (prod/cons)
	- Inizia processo consumatore all'avvio
		I.	preleva la stringa
		II.	/queue/error se tipo = 2
			/queue/info altri casi

Error Checker:
	I.	prende dalla coda error
	II. 	controlla
	III.	mette su error.txt
	IV.	visualizza a video

Info Filter
	I.	se contiene 1
	II.	mette su coda info.txt
	III.	visualizza a video

