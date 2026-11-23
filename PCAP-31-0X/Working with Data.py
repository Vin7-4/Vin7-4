##############################################################################################################################
from io import Reader

#                                            W O R K I N G   WITH      D A T A

#                                                                                    IN PYTHON


##############################################################################################################################


#  PER APRIRE UN TXT piazza direttamente una cartella coi files che ti servono all'interno    >>>   c:\\Py3\\py3test.txt
#
#       open()       << << << <       file viene letto e aperto in mem
#
# .....lavori in corso.....
#
#      close()           << << << << <<        file txt alla fine delle operazioni viene chiuso
#
#
#      rd = open("<nomefile>.txt", "opt")       << << <<         op preliminare, rendiamo disp a py la lettura del txt che andremo a usare per le mod
#

#
# ****************************************************************************************     Formati
#

# --------------------------------------------------------   Array Format
#
# [
#     {
#         "id": 1,
#         "name": "John Doe",
#         "age": 25
#     },
#     {
#         "id": 2,
#         "name": "Jane Smith",
#         "age": 40
#     }
# ]


# ------------------------------------------------------------   Object with Nested Objects Format
#
# {
#     "users": {
#         "1": {
#             "name": "John Doe",
#             "age": 25
#         },
#         "2": {
#             "name": "Jane Smith",
#             "age": 30
#         }
#     }
# }


#
# ---------------------------------------------------------------------       lista opt
#
#    r         >> >> apri per lettura
#
#    w         >> >> apri per scritt
#
#    x         >> >> apri per apertura esclusiva fail se il file txt è già esistente
#
#    a         >> >> apri per sovrascrittura
#
#    b         >> >> apri in binary mode
#
#    t         >> >> (default) apri in text mode
#
#    +         >> >> apri per read / write(updating file) >> >> >> >> >> >> si usano anche in combinazione
#


# Es.

#   open("C:\\Py3\\py3test.txt", "a+")     #    << << < qui apre in sovrascrittura(opt a) e fa l'appending (opt +)
                                                    #                                        sovrascrittura + appending == " a+ "



#    --------------------------------------------------------------------------------------------------------------------------



print("\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°     working with TXT files     °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")




open("C:\\Py3\\py3test.txt", "r")

rd = open("C:\\Py3\\py3test.txt", "r")

print(rd.read())


#  output :
# ------------------------
# TEST
# -----------------------
# FILE
# TXT
# PROVA
# TEST
#
# Alla fine delle op il file viene chiuso con il method >> > close()

rd.close()

# -----------------------------------------------------------------------------------------------------   WITH
#
# statement(chiamato anche "context manager")
#                                si usa per gestire meglio il lavoro da fare sul txt
#




print("\n-------------------       Adding lines ad un txt   (WITH statement)       -------------------\n")



with open("C:\\Py3\\py3test.txt", "r") as data:       #     <<  gestisce e incamera in mem l'apertura del txt inglobando il tutto nella var "data"
     data.write('\n<aggiunta linea al txt>') #  << sovrascrive il txt con data.write tenendo presente di andare a capo con \n
#
# --- lettura risultato effettiva scrittura

data = open("C:\\Py3\\py3test.txt", "r")    #   << << << << << << < leggi( in mem) il file
print(data.read())    #   <<  echo a schermo(print della lettura)

data.close()


#
# -------------------------------------------- Gestione

#   >>>>    import csv       !!!!!    importa il package csv

#sf = open('C:\\Py3\\cust.csv') # <<  assegna var alla lettura del file.csv
 #       reading1 = csv.reader(sf)   # << << assegna var al metodo 'reader' dell 'attributo ' csv ' (il reader di csv legge il csv - contenuto nella var "sf")
#                                               >> > sampledata = list(sread) << <<  assegna a lista(sampledata) >> >> contiene la lettura del csv.reader(sf)

#   >> > sampledata << << << << << esegui "sampledata" come cmd


#   [['nome cosa cittÃ\xa0']]

# -----------------------------------------------------------------------------------------------------------------     print con lettura pedici
#
# >> > sampledata[1] >> >> >> >> >> becca la line 1
#
# >> > sampledata[1][3] >> >> >> >> >> > legge la line1 e prende il 3° dato presente
#
# ------------------------------------------------------------     utilizzo con WITH e list

import csv

with open('C:\\Py3\\cust.csv') as data:     #    ingloba l'apertura in var "data" ... csv_list = csv.reader(data)
                                                                                   # <<  legge tutto 'data'(che sarebbe il csv) con l'object ' read '                                                                                                                               e piazza in una list


     for row in csv_list:  #  << << per ogn lin dell list device = row[0] <<  a var 'device' assegna il dato0 della list
                                                                                    # location = row[2] <<  a var 'location' assegna il dato2
                                                                           #                                    della list(*ultimo dato del csv in questione)
      ip = row[1]   # << << << << < a var 'ip' assegna la line1



print(f"{device} is in {location.rstrip()} and has IP {ip}.") #      << << << << << << << << <       *.rstrip in location

data.close()

# viene utilizzato per non tenere presente(causa formattazione) spazietto bianco finale della line (l'ultimo dato in questo caso è la 2)


print("\n--------------------------     Add inlin a csv     ----------------------------------\n")




#- -----------------------------------------1.  crei il codice di inserimento

print("inserimento dati database relazionale dipendenti")

index = input("Inserisci index rel >_")

n = input("inserisci nome >_")

cogn = input("inserisci cognome >_")

m = input("inserisci mail >_")



#  - -----------------------------------------2.    crei lista di var


dip = [index, n, cogn, m]



#    - -----------------------------------------3.    utilizzo with statement


with open("C:\\Py3\\cust.csv", "a") as data:
      csv_write = csv.writer(data)
      csv_write.writerow(dip)

data.close()











