> [!example] Index
> [[#Overview]]
> [[#Caratteristiche]]
> [[#Protocol Buffer (protobuf)|Protobuf]] 

- [b] Riferimenti
>
> [core_concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
> [quickStart](https://grpc.io/docs/languages/python/quickstart/).
> [basic](https://grpc.io/docs/languages/python/basics/)
> Kasun Indrasiri, Danesh Kuruppu, "gRPC: Up and Running", O'Reilly Media, Inc.

# Overview
gRPC é un middleware RPC universale ad alte prestazioni e open source, può esser eseguito in qualsiasi ambinete, e viene utilizzato principalmente per:
- collegare microservizi 
- Dispositivi mobili e browser a servizi di backend
- generare librerie e client efficienti
È sviluppato da google ed ora é diventato un progetto di CNCF (Cloud Native Computing Foundation). É utilizzato da molte azien in sistemi distribuiti (google, Dropbox, sqare, Netflix)

# Caratteristiche

- **HTTP/2** per il trasport: streaming bidirezionale e multiplexing
- Protocollo buffer (protobuf) usato come IDL
	- genera codice automatico
	- prevenzione degli errori
- Supporto per:
	- autenticazione
	- streaming bidirezionale
	- controllo del flusso
- comunicazione bloccante e non bloccante
### HTTP/2
***da slide 6 a 9*** pdf 14

## Protocol Buffer (protobuf)

gRPC utilizza i protobuf come
- IDL per definire l'interfaccia del servizio
- Formato di interscambio dei messaggi

I protocol buffer sono basati sul modello Proxy-Skeleton (stub e server).
Essi sono un meccanismo oramai maturo di Google per serializzare i dati strutturati. Usano una rappresentazione binaria dei dati fortemente tipizzata.
I dati sono strutturati come messaggi:
- Messaggio: Piccolo record logico contenente una coppia di *nome-valore* chiamati campi
- I campi hanno numeri univoci: utilizzati per identificare i campi nel formato binario del messaggio.

.proto
```c //ho messo c solo perché lo colora bellino
// protobuf comment
syntax = "proto3" //versione del buf
package example.model //Il codice compilato viene inserito nel package

//tipo di messaggio (in entrata o uscita)
message Student {

//FieldType FieldName FieldTag

string student_id = 1 
string first_name = 2
string last_name = 3
string address = 4
string is_joined = 5
}
```

In python la direttiva package viene ignorata; ma viene fortemente consigliato aggiungere il package come direttiva nel file .proto

- - -
# Python 
## Installer
```bash
pip install grpcio
pip install grpcio-tools
```
## Esempio
```c helloworld.proto

syntax = "proto3";

package helloworld;
//Definizione del servizion chiamato Greeter

service Greeter {
	//send a greeting
	rpc SayHello (HelloRequest) returns (HelloReply) {}
}

//messaggio di richiesta
message HelloRequest{
	string name = 1;
}

//messaggio di ritorno
message HelloReply{
	string message = 1;
}
```

```bash //Compilazione del file proto nella stessa directory
python -m grpc_tools.protoc --python_out=. --pyi_out=. --grpc_python_out=. helloworld.proto
```

```bash //Compilazione del file proto in directory diversa
python -m grpc_tools.protoc -Iprotos --python_out=. --pyi_out=. --grpc_python_out=. protos/helloworld.proto
```

La compilazione genera due file:
- helloworld_pb2.py: che contiene il codice protobuf per popolare, serializzare e recuperare i tipi di messaggi
- helloworld_pb2_grpc.py: che contiene
	- interfaccia proxy
	- Interfaccia Skeleton

```python
class GreeterStub(object):
	"""The greeting service definition.
	"""
	def __init__(self, channel):
		"""Constructor. Args: channel: A grpc.Channel.
		"""
		self.SayHello = channel.unary_unary('/helloworld.Greeter/SayHello', request_serializer=helloworld__pb2.HelloRequest.SerializeToString, response_deserializer=helloworld__pb2.HelloReply.FromString, _registered_method=True)


class GreeterServicer(object):
	"""The greeting service definition.
	"""
	def SayHello(self, request, context):
		"""Sends a greeting
		"""
		context.set_code(grpc.StatusCode.UNIMPLEMENTED)
		context.set_details('Method not implemented!')
		raise NotImplementedError('Method not implemented!')
```

```python 
#server.py
from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

### crea una classe Greeter che implementa il servizio GreeterServicer
### in questo caso implementiamo il metodo SayHello

class Greeter(helloworld_pb2_grpc.GreeterServicer):

	def SayHello(self, request, context):
	
		print("[server] SayHello method invoked, returning response...")
		return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

### implemento il metodo serve() che sarà invocato come prima funzione dal main

def serve():
	# mi istanzio un oggetto server da grpc
	
	# ALERT: i ThreadPool sono quelli del package concurrent e non multiprocess. Alcune diff in: https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	
	# aggiungo al server l'oggetto istanza del mio sercizio Greeter
	helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

	# faccio il bind con localhost al primo porto libero
	port = server.add_insecure_port("0.0.0.0:0")
	# avvio il server
	server.start()

	print("Server started, listening on " + str(port))
	# attendo che il server termini
	server.wait_for_termination()

if __name__ == "__main__":
serve()
```

```python 
#client.py

from __future__ import print_function
import logging
import sys
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
	# NOTE(gRPC Python Team): .close() is possible on a channel and should be
	# used in circumstances in which the with statement does not fit the needs
	# of the code.
	
	print("Will try to greet world ...")
	
	# creo un canale verso il server RPC
	with grpc.insecure_channel("localhost:" + sys.argv[1]) as channel:
		# creo uno stub (GreeterStub, ovvero ${NOMESERVIZIO}Stub) per invocare tutti i metodi implementati nel servizio
		stub = helloworld_pb2_grpc.GreeterStub(channel)
		response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
		print("[CLIENT] SayHello invoked Greeter client received: " + response.message)

if __name__ == "__main__":
	run()
```

# Tipi di gRPC
In gRPC sono supportati 4 tipi di RPC call:
- **RPC semplice (unary)**: Il client attende una singola risposta  dal server
  `rpc SayHello (HelloRequest) returns (HelloReply) {}`
- **Streaming RPC lato server**: Il server risponde al client un flusso di messaggi; il client legge finché non terminano i messaggi
 `rpc SayHello (HelloRequest) returns (stream HelloReply) {}`
- **Streaming RPC lato client**: Il client invia uno stream di messaggi al server il quale restituisce un solo messaggio di risposta
   `rpc SayHello (stream HelloRequest) returns (HelloReply) {}`
- **Bidirectional Streaming**: Sia il client che il server sfruttano uno stream di messaggi, quindi il server potrebbe o rispondere man mano che riceve i messaggi o attendere l'arrivo di tutti i messaggi e poi rispondere
   `rpc SayHello (stream HelloRequest) returns (stream HelloReply) {}`

Per inviare uno stream di messaggi viene utilizzato il metodo **yield** al posto del **return**

# Limitazioni di gRPC
- Supporto limitato nel browser
	- Mancanza del supporto completo di HTTP/2
	- gRPC-Web può fornire il supporto al browser ma con caratteristiche limitate
- Formato non human-readable
	- Protobuf é efficinte nell'invio e nella ricezione ma non ha un formato leggibile
	- Gli sviluppatori hanno necessita di strumenti aggiuntivi