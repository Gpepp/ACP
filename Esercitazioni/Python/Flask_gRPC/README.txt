Sensore:
	- id
	- data_type (temp/press)
Misurazione:
	- sensor_id
	- data


a. Controller (Flask):
	- /sensor (post): {
				"_id": 10,
				"data_type":"temp"
			  }
		return {"result": "success"} NB. Potrebbe fallire se il sensore é giá registrato
		Salvare su MongoDb collection Sensors

	- /data/<data_type> (post): {
					"sensor_id":10,
					"data": 30
				    }
		return {"result": "success"} NB. Potrebbe fallire se data_type errato
		Salvare su MongoDb colleciton temp_data o press_data

b. Sensors -> Simula un set di sensori
	I. 	5 thread:
			- id incrementale che é id del sensore
			- datatype scelto a caso
			- registra il sensore con /sensor post
			- effettua 5 misurazione /data/data_type -> num casuale tra 1 e 50

c. Statistics (server gRPC): -> statistics.proto
	- rpc getSensors(Empty) returns (stream Sensor) -> ritorna i dati dei sensori registrati per il controllor dalla collection Sensors con le info dei singoli sensori Sensor
	- rpc getMean(MeanRequest) reutrns (StringMessage) -> Calcola la media delle misuarazioni fatta da un singolo sensore.

d. Dashboard: -> client gRPC 
	I. 	Richiede le info dei sensori con getSensors
	II.	per ogni sensore chiede la media
