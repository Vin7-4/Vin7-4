################################################################################################


#                             T U P L E S     &      D I C T I O N A R I E S


##################################################################################################




# Python data ---
#             1. MUTABLE : liberamente aggiornabile >>> OPERATION IN SITU   (lists)
#             2. IMMUTABLE : non è aggiornabile nel corso dell'esecuzione del code   (tuples)



#--------------------------------------------------------------------------------------------------------------




####################################################################  TUPLES (immutable)


##########  utilizzo delle parentesi tonde




# PyDev console: starting.
# Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32

#  >>> t1 = (1., 2, 77, 4)
#  >>> type(t1)
# <class 'tuple'>

x = 99
y = 666

tup1 = (1, 10, 100, 1000)
tup2 = (.5, 2., .3, 9.)
tup3 = (3, 78, 90, -5, 8)
tup4 = (4., )
tup5 = (5, x)
tup6 = (y, -6)





##############################################  OPs sui tuples






tup1 = (1., 2, 77, 4)
tup2 = (4, 8, 10, 55, 7.)
tup3 = (90, .2, 1., 33, 56)

print(5 in tup1)  # False
print(77 in tup1)  # True
print(5 not in tup1)  # True






######################### trasforma tupola in lista





l = list(tup1)

print(type(l))  # output :  <class 'list'>




######################### trasforma lista in tupola


lst = [1, 2, 3, 4, 5]
t1 = tuple(lst)
print("Lista divenuta tupola :", t1)

# Lista
# divenuta
# tupola: (1, 2, 3, 4, 5)
#
# >> > print("Type di t1 > ", type(t1))
# Type
# di
# t1 > <
#
#
# class 'tuple'>




# ****************************************************




tup0 = tup1 + tup2
print("Concat tup1 + tup2 :", tup0)  # output : Concat tup1 + tup2 : (1.0, 2, 77, 4, 4, 8, 10, 55, 7.0)

tup00 = tup3 * 2
print("tup3 moltiplicato per 2 :",
      tup00)  # output : tup3 moltiplicato per 2 : (90, 0.2, 1.0, 33, 56, 90, 0.2, 1.0, 33, 56)

print("len di tup2 :", len(tup2))  # output : len di tup2 : 5




print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T  assegnazione fast a var  ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")



(a1, b2, c3) = (1, 2, 3)

print(a1)
print(c3)




print("\n------------LAB tuple-ops---------\n")

# >>> type(tup2)
#     <class 'tuple'>


print(tup1[0])
print(tup1[0:1])  # 1
print(tup1[-2])  # 100
print(tup1[1:])  # (10, 100, 1000)
print(tup1[2:])  # (100, 1000)

# non esiste tup1.append()


print("-------------------------\n")



for elem in tup1:
    print(elem, end=", ")




print("-------------------------\n")



for elem2 in tup2:
    print(elem2, end=", ")



print("-------------------------\n")




print(len(tup1), "\n")
print(len(tup2), "\n")




print("-------------------------\n")




t1 = tup1 + (77, 21)

print(77 in tup1)  # 77 non è presente nel tuple tup1
print("Len tup1 =", len(tup1))

t3 = (32, 90, -5., .12) + tup3

print("t3 updated : ", t3)
print("(tuple tup2)...e il -5 è presente?", -5 not in tup2)
print("(tuple tup3) --eghein...e il -5 è presente?", -5 not in tup3)

tup4, tup5, tup6 = tup6, tup5, tup4

print("Cambio ordine di tup4 >> tup6 -- :", tup4, tup5, tup6)




#########################################################################################################################


####################>>>>>>>>>>>>>>>>  DICTIONARY (dict)   #####################


# ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ
# utilizzo
# delle
# parentesi
# graffe
#
# d = {'cat': 1, 'dog': 2}
# type(d)
# <
#
# class 'dict'>
#
#
# methods(con
# exempols
# scorri
# giù - -fungono)
#
# .keys()
# .items()
# .get('value')  # restituisce value della key in question
# .count()  # conteggio delle key relative al value   ex. print(dict['<value>'].count('<key>'))
#
# .values()  # aggiunge item
# .update()  # aggiunge item
# .copy()  # copia un dict
#
# .pop('value')  # elimina il value in questione (tra apici singoli ' ')
# .popitem()  # elimina ultimo dato
# .clear()  # pulisce tutto nel dict
#
# >> > type(dict1)
# <
#
# class 'dict'>
#
#
# stringhe
# conviene
# piazzare
# tra
# apici
# singoli
# ' '
#
# dict = {key1: value1, key2: value2, ....}




print("-------------------------\n")
print(" Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж  DICTIONARY (dict)\n")




print("------------LAB® personal™---------\n")

print("Era del Mesozoico")
print("Triassico", "Giurassico", "Cretaceo")

dict1 = {'Deinocheirus†': 3, 'T.Rex†': 2, 'Dimethrodon†': 1, 'Mamenchisaurus†': 3, 'Dreadnaught†': 3}

dict_num = {'♀ Mr Ripley': 347895562,
            '♂ Miss Jackson': 3339087451,
            '♂ Suzy (secretary)': 22657854310,
            '♀ Francis Ford Coppola': 5551234568}    #     hanging indent

dict_trad = {'cane': 'dog', 'cavallo': 'horse', 'gatto': 'cat', 'orso': 'bear'}

empty = {}
dict_select = {'Deinocheirus†': 3,
               '♂ Suzy (secretary)': 22657854310,
               'orso': 'bear', 'Dreadnaught†': 3,
               '♀ Mr Ripley': 347895562,
               'cavallo': 'horse'}  # hanging indent

print(dict1)
print(dict_num)
print(empty)

print("Len del dict1 :", len(dict1))


print("\n------------LAB® personal™----ordine del print rispetto al codigo-----\n")
print("\nOrdine nel code --", "cane>", "dog", "cavallo>", "horse", "gatto>", "cat", "orso>", "bear",
      "\nOrdine printato da Py3 : ", dict_trad, "☻ (dio porco)")



print("\n------------LAB® personal™----12-----\n")




print(dict1['Deinocheirus†'], "miticoho")
print(dict1["T.Rex†"])
print("\nNumero di cell az di Miss Jackson -> ", dict_num["♂ Miss Jackson"])
print(dict_trad['cavallo'])




print("\n------Ѱ------‰   LAB® personal™   ‰----100---Ѱ--\n")


ʯ = 0

for w in dict_select:
    if w in dict1:
        print(">>>>>>>>>>>>>   !!! beccato !!!!", w, "è presente nel dictionary dei dinosauri\n")
        ʯ += 1
        print("\nBeccato il dato presente!", "HIT #", ʯ, "\n**********************")
    else:
        print("\n", w, "non è presente nel dictionary dei dinosauri, mannaggia la madonna!\n")
    print("Nel dict prescelto sono presenti", ʯ, "dati uguali (dio maiale)")




print("\n------Ѱ------‰   LAB® personal™   TRAD---Ѱ--\n")




Д = 0

for k in dict_select:
    if k in dict_trad:
        print(">>>>>>>>>>>>>   !!! beccato !!!!", k, "->", dict_select[k])
    else:
        print("\n", k, "non è presente nel dictionary dei dinosauri, mannaggia la madonna!\n")





print("\n------------  LAB ----becca la key corrispondente-----\n")




dict_dino = {'Deinocheirus†': 3, 'T.Rex†': 2, 'Dimethrodon†': 1, 'Mamenchisaurus†': 3}

for Д in dict_dino.keys():
    print(Д, "->", dict_dino[Д])
    if dict_dino[Д] == 3: print("sei del Cretaceo!!\n")
    # print("--- Jurassic Selection ---")

    # if dict1.keys(self="2") : print("\nBeccato dinosauro del Giurassico! E' il mitico", Д)
    # else: print("\nCiao", Д, "mi spiace ma non sei del Giurassico... ma potresti essere del Cretaceo come il Deinocheirus!\n")




print("\n------------  LAB usando items (value) & keys together------becca item(value) corrispondente-----\n")




for ita, eng in dict_trad.items():
    print(ita, "->", eng)
    if ita == 'cavallo': print("No mistèr! u cavallo no ll'orso!!! ")




print("\n------------  LAB dinosauri ordinati---------\n")




for Д in sorted(dict_dino.keys()):
    print(Д, "->", dict_dino[Д])  # py3 will do its best!   in questo caso piazza in ordine alfabetico





print("\n----Ɣ--------  LAB -----moddⱯ & cambiⱯ----\n")

dict_trad2 = {'cane': 'dog', 'cavallo': 'horse', 'gatto': 'cat', 'orso': 'bear', "serpente": "snake",
              "uccello": "birdyyysssss"}

print("Ðictionary Ꞷ :", dict_trad2)
print("Prima ->", dict_trad2['uccello'])

dict_trad2['uccello'] = 'bird'
print("Ðøpø ->", dict_trad2['uccello'])
print("Ðictionary Ɐggiornato Ꞷ :", dict_trad2)





print("\n------------  LAB -----becca .values----\n")




for ꞵ in dict_trad2.values():
    print(ꞵ)
    print("Ñome item scomposto in lettere e riordinato alfabeticamente :", sorted(ꞵ), "\n")

#  tenedo presente un riordino (determinato da py3 allabbene emmeglio),
# genera una lista con le lettere che compongono il value in ordine alfabetico





print("\nЖ Ж Ж Ж Ж Ж Ж Ж --- LAB® ---  Ж Ж Ж Ж Ж Ж Ж\n")




print("Ðictionary Ꞷ :", dict_trad2)
dict_trad2['swan'] = 'cygne'

print("\nAggiungo Cigno (di Caianiello)\n")
print("Ðictionary Ɐggiornato Ꞷ :", dict_trad2)

print("\n------------  LAB ----     update-----\n")

print("Ðictionary Ꞷ :", dict_trad2)
dict_trad2.update({'anatra': 'oca canadese'})
print("\n  >>>>>   Aggiungo l'oca canadese (diahane sta tupolas è venuta troppo massella...)\n")
print("Ðictionary Ɐggiornato Ꞷ :", dict_trad2)






print("\n------------  LAB ----elimina dato (ultimooooo) dalla tupola-----\n")




dict10 = {'cane': 'dog', 'cavallo': 'horse', 'gatto': 'cat', 'orso': 'bear', 'serpente': 'snake', 'uccello': 'bird',
          'swan': 'cygne', 'anatra': 'oca canadese'}

print("Ðictionary Ꞷ :", dict_trad2)

dict10.popitem()

print("Ðictionary Ɐggiornato Ꞷ :", dict10)

print("\n------------  LAB ----elimina dato (ultimooooo) dalla tupola-----\n")

dict10.pop('gatto')

print("Ðictionary Ɐggiornato Ꞷ2 (elimina gatto):", dict10)

#  dict_trad2.pop('dog')   #  è una ky e non un value >>  da' errore

#  print("Ðictionary Ɐggiornato Ꞷ3 :", dict10)

dict1 = {'cane': 'dog', 'cavallo': 'horse', 'gatto': 'cat', 'orso': 'bear', 'serpente': 'snake',
         'uccello': 'bird', 'swan': 'cygne', 'anatra': 'oca canadese'}

print("\n------------  LAB™  ----copy-----\n")

print("len prima :", len(dict1))
d1 = dict1.copy()

print("\n printo dict copied : ", d1)
print("\nlen copiata :", len(d1))

d1.clear()

print("Dict con il .clear --pulisce todo >>>", d1)

d1 = dict1.copy()

print("\n------------  LAB™  ----get-----\n")

print("Key associata al value 'anatra' ?_>", d1.get('anatra'))
print("Key associata al value 'gatto' ?_>", d1.get('gatto'))

d1.update({'duck': 'canard'})

print("\n----   Segue new d1 dictionary (dopo il .clear e .copy):\n", d1)
print("tra parentesi ovviamente signore porco\n")

print("\n------------  LAB™  ----count-----\n")

di01 = {'cane': 'dog', 'cavallo': 'horse', 'serpente': 'snake'}

print(di01['serpente'].count('snake'))  # restituisce 1
print(di01)

print("\n------------  LAB™  ----replace-----\n")

# print(di01['serpente'].replace('snake', 'corn_flassss'))
print(di01, di01['serpente'].replace('snake', 'snake---'))

di01['cane'].upper()
print(di01)

print("\n------------          ---------")
print("\n------------  LAB™ namba 1 ---------\n")

school_class = {}
while True:
    name = input("Inserisci nome studente ?>_ ")
    if name == '':
        print("dio impestato!")
        break

    score = int(input("Immetti votazzione di questo rimbambito (nato con parto anale) ?>_ "))
    if score not in range(0, 11):
        print("dio porco!")
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

    for name in sorted(school_class.keys()):
        adding = 0
        counter = 0
        for score in school_class[name]:
            adding += score
            counter += 1
        print(name, ":", adding / counter)  # la media dei voti la calcola con adding/counter







#########################################################################################################################


####################>>>>>>>>>>>>>>>>  S E T S (SET)   #####################


#    collection NON ordinata    SENZA  key:value


































