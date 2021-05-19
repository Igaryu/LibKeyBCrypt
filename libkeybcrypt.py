# -*- coding: utf-8 -*-
import sys,os,getpass

    
def cls():
	if os.name=='posix':
		os.system('clear')
	else:
		os.system('cls')

def Allarme(n):
    print (n * chr(7))

#
# Verifica della presdenza del modulo python-bcrypt. Deve essere presente perché se ne usano 
# le funzioni per generare una chiave, o confrontare la chiave con l'input dell'utente
# se non presente viene interrotta la procedurar perché senza non può ovviamente funzionare
#

try:
    import bcrypt
except ImportError:
        Allarme(5)
        print "\n\n*** Attenzione !!!"
        print "------------------\n"
        print "\tPer poter utilizzare questa libreria devi avere installato il modulo brcypt"
        print "\tDa un analisi del tuo sistema non riuslta essere installato!!\n"
        print "\tPer installarlo in Debian, o derivate, o in MacOSX, esegui il seguente comando:\n"
        print "\t\tpip install python-bcrypt.\n" 
        print "\tDopo l'installazione rilancia il programma.\n"
        sys.exit(-9)

#
# Funzione presa in prestito dalla libreria getpass. Mi serviva solo per otenere un input mascherato
# durante la digitazione.
#
# Unico controllo sulla password al momento è sulla lunghezze che non puà essere inferiore a 8 char
# E' posssibile, cmq, inplementare facilmente altri controlli per pretendere una password o pass
# phrase accettabile.
#
def getpasswd():
        passwd=getpass.getpass('Password: ')
        if len(passwd)==0:
           Allarme(4)
           print "Attenzione: password non può essere nulla!!!"
           return -1
        elif len(passwd)<8:
           Allarme(4)
           print "Attenzione: password non può essere di lunghezza inferiore ad 8 caratteri!!!"
           return -1

        else:    
           return passwd

#
# Verica la presenza di un eventuale file chiave, non il contenuto.
#
def ChekIfExists(NomeFile):
    if os.path.isfile(NomeFile):
        return True
    else:
        return False

#
# Viene aperto il NomeFile, letta la chiave dal file che la contiene strippando
# il \n di coda alla riga, poi viene chiesto all'utente di digitare una password
# e questa viene confrontata con l'HASH della chiave. Se corrisponde viene  
# restituita al chiamante la password, altrimenti una stringa "Password Errata".
#

def GetKey(NomeFile):
    fp=open(NomeFile,"r")
    Chiave=fp.readline().encode('utf-8').rstrip('\n')
    fp.close()
    ChiaveInChiaro=getpass.getpass("Digita password per accesso generale: ").encode('utf-8')

    if bcrypt.checkpw(ChiaveInChiaro, Chiave):
        return ChiaveInChiaro
    else:
        return "Password errata!!"
    

#
# Generazione del file contenente la chiave HASH. Viene richiesta una password all'utente:
# se non viene passato il controllo sulla lunghezza visutalizza un messaggio e torna al chiamante
# un vaore di -2
# se il risultato del tes è posivito allora viene:
# Aperto un file in socrascrittura, generata e scritto, l'hash BCrypt corrispondente, nel file
# Viene chiuso il file e tornato al chiamante il valore  numerico 0 (zero)

def GenKeyFile(NomeFile):
    ChiaveInChiaro=getpass.getpass("Digita password principale per l'accesso generale: ").encode('utf-8')
    if len(ChiaveInChiaro)<8:
        Allarme(2)
        print "La password non puo essere minore di 8 caratteri!!!"
        return(-2)
    else:
        fp=open(NomeFile,"w")
        fp.write(bcrypt.hashpw(ChiaveInChiaro,bcrypt.gensalt()))
        fp.close()
        return(0)
