> [!example] Index - [[0 - Index|Home]]
> [[#Sistemi Distribuiti|Sistemi distribuiti e EAI]]
> [[#Middleware|Concetto di Middleware]]
> >[[#Proprietà|Trasparenza]]
> > [[#Tecnologie middleware|Modelli e tecnologie]]
>
> [[#Esempi di Middleware]]

> - [i] Domini di Applicazione su Rete
> - Finance and commerce: Amazon, eBay, payPal ...
> - Information society: World Wide Web, search engine (Google/Yahoo)
> - Entrtainment: gaming, streaming
> - Transportation: location, traffic management, web-based
> - Science: grid computing
> - Utility e cloud-Computing

# Sistemi Distribuiti
> - [f] Definizione:
>	- Un sistema Distribuito é un sistema i cui componenti, localizzati in computer econnessi in rete, comunicano e coordinano le loro azioni attraverso lo scambio di messaggi
![[Sistemi_Distribuiti.png]]

- [k] Implicano:
	- Elaborazione concorrente
	- Assenza di clock globale
	- Malfunzionamenti indipendenti

## Sistemi distribuiti eterogenei
I sistemi distribuiti generalmente sono distribuiti. L'eterogeneità dei computer e delle tecnologie è da considerarsi la "norma" non l'eccezione.

In ambiente distribuito vari fattori aumentano la complessità dello sviluppo di software di qualità:
Sono distribuite su una rete di calcolatori di caratteristiche differenti, dotati di HW e SO differenti e incompatibili. Pertanto occorre adoperare linguaggi di programmazione differenti.

I dati sono distribuiti e condivisi da applicazioni locali e remoti.

Nello sviluppo di software su rete occorre fronteggiare problematiche quali:
- sicurezza
- guasti
- contesa e condivisione delle risorse

## EAI (Enterprise Application Integration)

Sistemi complessi raramente vengono sviluppati integralmente. Tipicamente partono da sistemi già funzionanti.
L'integrazione di sistemi informativi sviluppati in momenti, ed operanti su piattaforme eterogenee. Si richiede di:
- utilizzare applicazioni di terze parti
- riutilizzare applicazioni esistenti

L'integrazione di applicazioni EAI é un processo più complesso dello sviluppo ex novo.
Lo sviluppo del software, la programmazione é una faase critica del ciclo di vita del software sia in termini di competenze che di risorse
 - [k] Assume maggiore importanza la capacità di adattare componenti esistenti e non originariamente pensati per interoperare

Per questo molte tecnologie *middelware* sono nate con l'obiettivo di fornire una soluzione al problema dell' EAI

# Middleware
> - [f] Definizione
> Con il termine middleware si intende uno strato software interposto tra il sistema operativo e le applicazioni in grado di ***fornire le astrazioni ed i servizi*** utili per lo svlippo di applicativi distribuiti

Lo strato middleware offre ai programmatori *librerie di funzioni* o *middleware API (Application Programming Interface)* ingrado di mascherare l'eterogeneità dei sistemi su rete

- [f] Le piattaforme middleware vengon anche definite "Glue Technologies", evidenziando la loro caratteristica di tecnologie di integrazione di applicazioni

## Proprietà

Il livello middleware può mascherare le eterogeneità mediante meccanismi di:
- Trasparenza del sistema operativo:
	Operando al disopra del sistema operativo le API middleware possono essere definite in maniera indipendente da esso
- Trasparenza del linguaggio di programmazione
	La comunicazione tra componenti sviluppati in linguaggi diversi pone problemi connessi alle differenze tra i *tipi di dato supportati* o alle differenze di *scambio dei parametri di invocazione*.
	I middlware possono consentire l'interoperabilità definendo un sistema di tipo intermedio e regole di scambio dei messaggi
- Trasparenza della locazione
	Le risorse dovrebbero essere accessibili a livello logico senza conoscere l'effettiva posizone fisica. **Lo strato middleware deve farsi carico della localizzazione**
- Trasparenza della migrazione
	Un dato durante la sua vita potrebbe essere migrato; pertanto il middleware può consentire l'acceso a componenti mobili sulla ree in maniere trasparente ai moduli client
- Trasparenza ai guasti
	Una elaborazione distribuita può fallire, pertanto é lo strato middleware che puó offrire ai programmatori meccanismi ad alto livello per mascherare guasti
- Trasparenza alla replicazione
	Le tecniche di replicazione vengono utilizzate per realizzare politiche di **tolleranza ai guasti** ma anche per **migliorare le prestazioni**
- Trasparenza delle implementazioni commerciali
	Sono conformi allo standard e quindi garantiscono l'interoperabilità

## Tecnologie middleware
Nell'ultimo decennio sono state realizzate diverse tipologie di piattaforme middleware.
I principali modelli sono:
- Chiamata a procedura remota (RPC, Remote Procedure Call)
- Scambio di messaggi (MOM, Message-Oriented Middleware)
- Transazionale (TP, Transaction Processing)
- Spazio delle tuple (TS, Tuple Space)
- Accesso remoto ai dati (RDA, Remote Data Access)
- Oggetti distribuiti (DOM, Distribuited Object Middleware)
- Componenti (CM, Component Model)
- Servizi web (WS, Web Services)

### Tassonomia
- Orientati all'accesso ai dati:
	- RDA (ODBC, JDBC, ORACLE DB INTEGRATORS)
	- TP (X/Open DTP)
- Orientati alla comunicazione:
	- [[#Il Modello RPC|RPC]] (SunRPC, OSF DCE RPC)
	- MOM (IBM MQSeries, AMQP, JMS, DDS)
	- TS (Linda, JavaSpaces, Jini)
	- DOM (Java/RMI, OMG COBRA, MS DCOM, .NET remoting)
	- CM (OMG CCM, EJB)
	- WS (JAX-WS, MS WCF)

#### Il Modello RPC

Nel modello RPC la comunicazione è intrinsecamente di tipo sincrono e bloccante.
> [!warning] NotaBene
> La disponibilità di meccanismi no bloccanti (asincroni) é da considerarsi una eccezione

##### Funzionamento
In fase di compilazione vengono generate automaticamente delle interfacce dette ***stub***, una lato client e una lato server. Essi implementano in maniera trasparente lo scambio di parametri. A tal fine gli stub accedono direttamente ai servizi.

###### Ruolo degli Stub
- Lato Client
	1. Preleva i parametri di scambio
	2. Impacchetta in un messaggio, affidato al software di rete per la trasmissione
	3. Attende la risposta che indica il completamento della procedura remota
	4. Spacchetta il messaggio per i parametri d'uscita
	5. Restituisce i parametri al programma chiamante che riprende il controllo
- Lato Server
	1. Attende un messaggio di invocazione della procedura (dal software di rete)
	2. Spacchetta il messaggio per i parametri di scambio
	3. Trasmette i parametri alla procedura chiamata, cui cede il controllo
	4. Riprende il controllo al termine della procedura, ed impacchetta i parametri d'uscita in un messaggio di riposta al client
	5. Invia il messaggio di risposta e si mette in attesa di una nuova richiesta

Il programma sia chiamante che servente invocano delle procedure a tutti gli effetti locali


###### Marshalling dei parametri
Le operazioni di impacchettamento e spacchettamento  svolte dagli stub prendono il nome di *marshalling* e *unmarshalling*
Il marshalling consiste:
- conversione di formato:
  per tenere conto deelle differenze di rappresentazione tra client e server
- Serializzazione dei dati:
  In modo che vengano trasformati in uan sequenza di byte secondo un formato compreso da client e server

La trasmissione avviene secondo due tipologie:
- External data Representation (Formato Esterno):
  I dati sono converti in un formato concordato tra sender e reciver. Il reciver poi converte i dati nel proprio formato
- Formato del Sender
  I dati sono trasmessi nel formato del sender e sono accompagnati da un'indicazione sul formato

###### Semantica delle RPC

Nella comunicazione ci possono essere dei malfunzionamenti che possono causare:
- perdita dei messaggi
- caduta del nodo servente dopo la ricezione ma prima dell'invio della risposta

Allora possono essere adottate delle semantiche:
- **Exactly Once**: La procedura viene eseguita una e una sola volta
- **At most Once**: Non si può garantire che la procedura sia stata eseguita ma se e stata eseguita essa é stata eseguita una sola volta
- **At least once**: la procedura viene seguita almeno una volta
- **Zero or more**: Non é possibile dire quante volta sia stata eseguita quella procedura

[[#Esempio RPC - Sun RPC]]


#### Il Modello MOM (Orientato ai Messaggi)
Il modello a scambio di messaggi si basano sull'astrazione di una *coda di messaggi* - rappresenta il modello di **mailbox**.
Nel modello MOM la comunicazione é tra pari (_peer-to-peer_) di tipo produttore consumatore, tipicamente asincrona.
> [!warning] NotaBene
> Alcuni implementano messaggi di tipo **sincrono**

I sistemi MOM possono adottare modelli *publish-subscribe* in cui:
- **produttori**: pubblicano i messaggi differenziati per tipo
- **consumatori**: si dichiarano interessati ai messaggi
- [p] Le piattaforme MOM sono adatte per applicazioni guidate dagli eventi (event-driven)
      al verificarsi di un evento un *produttore* affida al middleware la responsabilitá di notificarne la disponibilitá ai processi.
      Molti processi MOM realizzano anche la persistenza dei messaggi.

Solitamente i MOM sono utilizzzati per rimpiazzare gli RPC dato che:
- [d] **RPC**: Le chiamate RPC sono sincrone e possiamo avere problemi di scalabilità
- [d] **RPC**: Le richieste arretrate rallentano il sistema
- [u] **MOM**: Utilizza un meccanismo asincrono per incrementare la scalabilità
- [u] **MOM**: Migrare da un server all’altro utilizzando i broker nel caso di fallimento di un server
##### Comunicazione indiretta
La comunincazione avvine tramite un intermediario, senza un accoppiamento diretto tra sender e reciver. La natura dell'inetrmediario dipende dall'approccio:
- *group communication*: un messaggio viene inviato ad un gruppo, quindi recapitato a tutti i membri
- *shared memory*: distribuited shared memory, ~tuple_space~
- **code di messaggi**: meccanismo point-to-point. Il messaggio in una coda viene prelevato da un solo reciver
- **publish-subscribe**: il Publisher genera messaggi, il Subscriber esprime interesse ad un certo topic

##### Code e Publish-Subscribe
Questi middleware sono noti come message-oriented middleware. I sistemi Publish-Subscribe sono noti anche come *distributed event-based system*.
Il MOM gioca il ruolo di intermediario (message broker) nella comunicazione indiretta basata su messaggi:
- garantisce lo scambio con tecniche di store-and-forward
- solleva il programmatore dai dettagli di basso livello ed espone le API come primitive (send-recive).


##### Aspetti chiave
Gli applicativi di send e recive possono risiedere su macchine differenti; La comunicazione avviene tramite la rete ed il MOM può conservare un messaggio finche la rete non diventa disponibile.
Le applicazioni potrebbero non essere attive contemporaneamente durante l'invio di messaggi, ma il sender non si blocca nell'attesa che il reciver riceva il messaggio (*comunicazione asincrona*)
##### Disaccoppiamento
I MOM fornsicono un meccanismo per l'integrazione flessibile e disaccoppiate di applicazioni distribuite:
- **Disaccoppiamento Spaziale**: Il sender non conosce l'identità del reciver
- **Disaccoppiamento Temporale**: Il sender e il reciver possono avere cicli di vita differenti

##### Evento e Notifica
La comunicazione indiretta é fortemente utilizzata per la propagazioene di eventi nei sistemi distribuiti:
- *Evento*: condizione rilevata e comunicata all'intermediario sotto forma di messaggio
- *Notifica*: L'atto di informare un insieme di applicazioni dell'occorenza dell'evento
###### observer
- Observer dichiare interesse agli eventi generati dal/nel subject attraverso la **sottoscrizione**
- subject rileve l'coccorenza di un evento e notifica agli ooservatori




[[#Esempio MOM - Activemq/Stomp]]

---
# Esempi di Middleware
>[!example] Index
>[[#Esempio RPC - Sun RPC]]
>[[#Esempio MOM - Activemq/Stomp]]

## Esempio RPC - Sun RPC

L'implementazione di RPC di Sun Microsystem prevede:
- su una macchina servente un programma che contiene una o più procedure invocabili. 
- Le procedure coesistono nello stesso ambiente e quindi possono condividere le variabili. 
- Su un unico nodo possono anche coesistere più versioni dello stesso programma. 
- Al client é sufficiente una tripla di interi (programma, versione, procedura) per poter identificare la procedura da invocare

### XDR
Nello stesso programma remoto é garantita la muta esclusione; al più una procedura può essere in esecuzione in un dato istante anche in presenza di più client. Per esternalizzare i dati viene utilizzato lo standard **XDR**(eXternal Data Representation)
A seconda della semantica scelta Sun RPC si basa su TCP o UDP:
- TCP
	- at least once
	- zero or more once
- UDP
	- exactly once
	- at most once
### Binding dinamico
Esso per consentire la trasparenza della locazione adotta il ***binding dinamico***, ossia:
- Il servente ottiene dinamicamente il numero di porta disponibile
- Il client non conosce iil porto finché non viene attivato il server
- Sul nodo servente gira un processo **RPC Port Mapper**che gestisce una lista dei server attivi
- all'attivazione di un programma il PortMapper registra la coppia (programma, porto)
- Il port mapper opera sul porto prefissato (111)
- Il client contatta il port mapper prima di eseguire la RPC e riceve il numero di porto

#### PortMapper
1. Crea una socket sul porto 111
2. Accetta richieste:
	- registrazione di programmi RPC (dai serventi)
	- ricerca di porto di programmi RPC (dai client)
3. Una volta che il client ha trovato il porto da utilizzare effettua la chiamata al proprio stub locale che contatterà lo stub servente opportuno tramite un componente chiamato *Dispatcher*
> [!warning] Dispatcher
> Sul nodo servente il Dispatcher si occuperà di inoltrare i messaggi agli Stub opportuni![[SunRPC_Dispatcher.png]]

---
## Esempio MOM - Activemq/Stomp
