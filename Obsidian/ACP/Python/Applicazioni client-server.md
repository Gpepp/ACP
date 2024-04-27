# Client/Server

Deve prevedere:
- Connessione
- Esternalizzazione dei dati
- Invio/ricezione
- Ricostruzione
Rischi:
- Sovrapposizione della logica *applicativa* con quella di *comunicazione*

## Client
- logica applicativa:
  Deve sfruttare i servizi messi a disposizione dell'interfaccia
- Interfaccia:
  Implementazione delle funzionalità di comunicazione
## Server
- logica applicativa:
  Deve implementare i servizi messi a disposizione dell'interfaccia
- Interfaccia:
  Implementazione delle funzionalità di comunicazione
  - SEPARARE i meccanismi di comunicazione/interazione con i client
# Proxy - Skeleton
Il **Proxy** ha il compito di implementare i meccanismi necessari ad instaurare una comunicazione per l'invio/ricezione dei parametri
## Proxy - lato Client
- Il servizio é fornito dall'*interfaccia* del server
- Duplice implementazione
	- ServerImpl -> implementa i servizi dichiarati nell'interfaccia
	- ServerProxy -> si fa carico dell'inoltro delle richieste
### Client
Il client possiede un riferimento ad un oggetto di tipo 'interfacciaServer' (ServerProxy); e lo usa in sostituzione del servizio reale

## Skeleton - lato Server
Lo Skeleton (come il client) si fa carico della comunicazione con il *Proxy lato client*
1. Riceve la richiesta
2. Sfrutta l'informazione ricevuta tramite socket
3. Effetua l'up-call al servizio (impl)
4. Riceve eventuali risultati
5. Invia una risposta al client
### Ereditarietà

- "skeleton.py": La classe astratta *Skeleton* implementa solo gli schemi di comunicazione ma lascia senza implementazione i metodi dell'interfaccia
- "serverImpl.py": sottoclasse dello skeleton e fornisce l'implementazione dei metodi astratti
### Delega
- "skeleton.py": La classe skeleton presenta al suo interno un riferimento all'interfacciaServer (delegante)
- 