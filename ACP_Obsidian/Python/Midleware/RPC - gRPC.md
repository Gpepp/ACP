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
- IDL per definire l'interfaccia del servizion
- Formato di interscambio dei messaggi

I protocol buffer sono basati sul modello Proxy-Skeleton (stub e server)


