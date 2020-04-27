#!/usr/bin/python 
# -*- coding: utf-8 -*-
from libkeybcrypt import *



cls()
fname="Key.dat"
if ChekIfExists(fname):
    print "File "+ fname + " esiste!!"
    ChiaveInChiaro=GetKey(fname)
    print ChiaveInChiaro
    sys.exit
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
