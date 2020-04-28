# LibKeyBcrypt ReadMe file
Questa libreria ha lo scopo di gestire la scrittura di una password/passphrase su un file e chiaramente scriverla in modo **crittografato**.
La libreria chiaramente permette sia la creazione di un file chiave, che la verifica di correttezza password leggendo un file chiave generato in precedenza.

Questa libreria è stata creata per rispondere ad una esigenza specifica, che sicuramente sarà occorsa a molti nel passare del tempo. La libreria è in Versione 1.0

Perché in Python? Perché io lavoro fondamentalmente in Python e, quindi, il problema mi si poneva in questo linguaggio. Nulla vieta, a chiunque, di modificarlo per trasportarlo in altri linguaggi che meglio conoscono.

Le funziono presenti, ed incluse, nella libreria sono:

- `cls()`
- `Allarme()`
- `getpassword()`
- `CheIfExists(NomeFile)`
- `GetKey(NomeFile)`
- `GenKeyFile(NomeFile)`

## `cls()`
Semplice funzione che, determinato l’ambiente in cui viene eseguito, sceglie come pulire lo schermo. Sono presenti le possibilità per Linux e MacOSX. Facile implementare quelle per *BSD o Windows

## `Allarme()`
Semplice funzione per attirare l’attenzione dell’utente.

## `getpasswd()`
Funzione che riceve una password da tastiera **oscurandola**.

## `CheckIfExsists(NomeFile)`
Tramite chiamata alla libreria di sistema `os` verifica se ***NomeFile*** esista o meno.


## `GetKey(NomeFile)`
Legge la chiave `bcrypt` da **NomeFile** e la confronta con l’input dell’utente: se  **corrisponde alla chiave**, quest’ultima viene restituita dalla funzione al chiamante; altrimenti viene ritornato al chiamante la stringa ‘Password errata!!’

## `GenKeyFile(NomeFile)`
L’utente deve dare in input la password che vuole salvare. **Se la password è minore, in lunghezza, di 8 caratteri** non viene accettata, e viene restituito al chiamante il valore -2. **Se la password è di 8, o più, caratteri**, viene creato, o sovrascritto, il ***NomeFile*** contenente una chiave generata da `bcrypt` per il successivo confronto durante gli accesi, e alla fine, viene chiuso il file. Viene tornato al chiamante il valore 0 (zero)

Ultima edizione di questo file 27/04/2020

