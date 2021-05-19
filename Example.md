# Uso di Example.py

## utilizzo di prova della libreria `libkeybcrypt` in un programma

Fasi eseguite dall’esempio:

* Viene importata la libreria
	` from libkeybcrypt import *`
* viene assegnato un nuoe file da gestire
  ``` 
  cls()
  fname="Key.dat" 
  ```
* Viene verificata l’esistenza del file e se presente viene chiesta e stampata la password:
  ```
     if ChekIfExists(fname):
	    print "File "+ fname + " esiste!!"
	    ChiaveInChiaro=GetKey(fname)
	    print ChiaveInChiaro
	    sys.exit
  ```
* Se non esiste viene chiesto se si vuole generare un file crittografato con la password e se sì, si procede a chiedere la password e invocare la funzione `GenKeyFile()` che può tornare tre valori:
   1. 0 = creazione ok
   2. -2 Lunghezza password inferiore agli 8 caratteri
   3. -999 errore generico di creazione del file.
  Quindi:
  ```
  else:
    print  "File "+ fname + " NON esiste!!"
    SiNo="z"
    while (SiNo not in "SN"):
        SiNo=raw_input("Vuoi creare una password generale per l'appliczione? [S/N] ").upper()
    if SiNo=="N":
            sys.exit(-8)
    else:
        tmp=GenKeyFile(fname)
        if tmp==0:
            print "File generato con successo !!"
            sys.exit(0)
        elif tmp == -2:
            print "Password inferiore alla lunghezza richiesta [8 char]!!"
            sys.exit(-2)
        else:
            print "Errore generico nella creazione del file chiave!!!"
            print "Contattare lo sviluppatore."
            sys.exit(-999)

 _

Ovviamente è possibile modificare i limiti, minimi, per la validità della password dalla libreria stessa. Possono essere aggiunte regole come minimo numero di caratteri alfabetici, numerici, interpunzione e caratteri speciali.

La scelta è vostra.