[Riferimenti](https://docs.python.org/3/library/socket.html)

> [!example] Index - [[0 - Index|Home]]
> [[#Internet]]
> [[#Socket]]
> [[Socket|Socket TCP e UDP]]
> [[Concurrency|Multi-thread]]

# Internet
È una rete di estensione mondiale  basata sul protocollo TCP/IP. La progenitrice è *Arpanet*, che in origine era stata create per:
- esigenze militari
- connettere università e centri di ricerca

Oggi internet costituisce uno strumento per:
- scambiare e ricercare informazioni
- sviluppare sistemi distribuiti
- connettere centinai di milioni di dispositivi

## Oggi
Internete é una rete di reti, dove i componenti principali per la connessione sono:
- *host* o *nodi*: dispositivi connessi
- *cavi*, *fibraottica*, *radio*: Link di comunicazione
- *Router*: dispositivi che instradano i messaggi attraverso la rete
Un esempio di reti di reti é il [*GARR*](http://www.garr.it/it/infrastrutture/rete- nazionale/infrastruttura-di-rete-nazionale)(Gruppo per l'Armonizzazione delle Reti della Ricerca)

## Comunicazione

### Identificazione in Rete

Ad ogni nodo é associato un indirizzo IP:
- IPv4: 32 bit
- IPv6: 128 bit
Attraverso gli indirizzi IP é possibile identificare un computer sulla rete ed inviargli i dati.
Tipicamente viene associato un nome agli indirizzi, e la traduzione é realizzata dai DNS (Domani Name Service)

### Routing
I dati end-to-end sono trasmessi in pacchetti (*IP datagram*) di dimensione massima di 65.535byte.
Ip é un servizio *Best-Effort* dato che i pacchetti potrebbero essere persi o potrebbero arrivare in ordine sparso.

### TCP 
Implementa un trasporto affidabile da sorgente a destinazione su IP
- Fornisce un flusso di byte, full-duplex
- Orientato alla connessione: 
	- Instaurazione, utilizzo, e chiusura di una connessione
- Preserva l’ordine, eliminando duplicati
- Implementa la ri-trasmissione dei pacchetti
### UDP
- Protocollo di trasporto non affidabile
- Molto simile al protocollo IP, ma offre la capacità di distinguere tra porte differenti nello stesso host
- Basato sul concetto di datagramma

# Socket
Meccanismo di comunicazione tra processi, eventualmente distribuiti su macchine differenti, basato sulla rete.
Una socket fornisce ai processi un meccanismo per l’accesso alla rete. Essa è caratterizzata da *Indirizzo IP* e *Numero di porto* del nodo e possono essere TCP e UDP

