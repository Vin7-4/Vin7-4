#######################################################################################################################


#                            LISTE  (list)

#                                                     &&    L I S Ts  in Advanced application
                              #                                        (fine form)


#######################################################################################################################


# x=0
# #    0 1  2 3  4
# l = [15,8,32,9,25]
#
# print("\n", l, "\n")


############################  lab 1


# del l[1]  # camcella il 2° num della list
# print(len(l)) # quindi list composta da 4 numeri
# print(l)      # [15,32,9,25]
# # da qui in poi errore ::  out of range  >> la list arriva max a l[3]
# #print(l[4])
# #l[4] = 1


######################  programma cancella il porco del signore


print("\n")
print("\n----------------")

print("Data la lista [15,8,32,9,25,59,11,32,99,1000] cancella un numero dalla lista\n")

l = [1, 2, 3, 4, 5]
print(l)
print("Lunghezza lista :", len(l))
print("\nUltimo numero della lista :", l[-1])

x = int(input("\nNumero da cancellare ?>_ "))
s = int(input("\ninserisci numero da sostituire al pivot (#3 list[2]) ?>_ "))
l[2] = s
print("\nlista aggiornata : ", l)

while True:
    y = 0
    print("\nnumero scelto :", x)
    for k in l:
        # print(k)
        if x == l[y]:
            del l[y]
            print("Lista aggiornata : Elimina", x, "e aggiorna pivot >>", l)
            print("Eliminazione ultimo elemento in corso...Fatto!\n")
            del l[-1]
            print("Lunghezza aggiornata :", len(l), "\nLista aggiornata : ", l)
            a = int(input("Incolla numero nella lista -- inserisci numero ?>_ "))
            l.append(a)
            print("Lunghezza aggiornata :", len(l), "\nLista aggiornata : ", l)
            print("\n")
            print("Procedo a inserire nuovi dati...\n")
            l.insert(0, 200)
            l.insert(1, 201)
            l.insert(-1, 444)
            print("Aggiunti i num 200 -- 201 -- 444\n  Lunghezza aggiornata :", len(l), "\n    Lista aggiornata : ", l)
            continue
        else:
            y += 1

    è = input("s per continuare -- tasto qualsiasi per uscire : ?>_ ")
    if è == "s":
        continue
    else: break


#
#
# k = []
#
# for i in range(5):
#     k.append(i+1)    # glued alla fine della lista
#
# print(k)
#
#


# ############################################################
#


# print(""
#       "\n---------------\n")
#
# j = []
# t = []
# p = []
#
# for i in range(5):
#     j.insert(0, i+1)
#     t.insert(1, i+1)
#     p.insert(2, i+1)# reversa i numeri nella lista con index = 0  >>  [5,4,3,2,1]
#                                                 #            = 1  >>  [1,5,4,3,2]
#                                                  #           = 2  >>  [1,2,5,4,3]   and so on...
# print(j)
# print(""
#       "\n---------------\n")
# print(t)
# print(""
#       "\n---------------\n")
# print(p)
#
#


# ####################################################  Somma numeri interni alla lista
#


# print(""
#       "\n---------------\n")
#
# q = [1,3,2,6,4]
# tot=0
#
# for i in range(len(q)): tot+=q[i]
# print("Lista : ", q)
# print("La somma dei numeri interni alla lista sarà :", tot)
# print("La radice quadrata sarà", tot**0.5)
#
# print(""
#       "\n---------------\n")
#


# ################################  Prog crea lista
#


# print("""
# ----------------------------------------------------------  \n\n\n****     Programma crea lista\n
# """)
#


# x = int(input("Inserisci lunghezza lista (q.tà di numeri presenti) ?>_ "))
# z = []
# k = 1
# y = range(x)
# tot=0
#
#
# for i in y:
#     w = int(input("Inserisci " + str(k) + "° numero : ?>_ "))
#     z.insert(k, w)
#     k+=1
# print("lista generata : ", z)
# print("---------------------\n")
# c = input("Vuoi sommare i numeri della lista? (digita s per sommare - tasto qualsiasi per uscire)>_ ")
#
# if c == "s" :
#     for i in range(len(z)): tot += z[i]
#     print("Somma totale : ", tot)
# else: exit(0)
#
#


# ################################  Prog sotituisci membri della list
#
# print("""
# ----------------------------------------------------------  \n\n\n****     Programma S.W.A.P.\n
# """)
#
# v = [3,7,1,55,9]
#
# v[0], v[4] = v[4], v[0]
# v[1], v[3] = v[3], v[1]
#
# v[2] = '?'
# print("Lista : ", v)
#
# ############################  con un bel po' di vars -- ribaltone tutale
#


# v = [3,7,1,55,9,11,34,5,41]
# #v = [0,1,2,3,4]
# n = len(v)
#
# print("Lunghezza", n)
#
# for i in range(n // 2) :
#     v[i], v[n-i-1] = v[n-i-1], v[i]
#     print("Passaggio " + str(i) + " lista aggiornata = ", v)
# print("\n-------------------\n")
# print("Lista finale : ", v)
#


#
# ###############################   Lista BEATLES

#
# from time import sleep
#
# print("""
# ----------------------------------------------------------  \n\n\n****     Programma BEATLES\n
# """)
#
# beatles = []
#


# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
#
# print("Formazione iniziale del 1960 : ", beatles)
#
# for i in range(3,4):
#     s = input("Vuoi aggiungere Stu Sutcliff?")
#     print()
#     beatles.append("Stu Sutcliff")
#     print(beatles)
#     sleep(5)
#     p = input("Vuoi aggiungere Pete Best?")
#     print()
#     beatles.append("Pete Best")
#
# print(beatles)
# print("Trascorrono gli anni...")
# sleep(4)
# print("1961...")
# del beatles[-1]
# sleep(3)
# print("Rimangono", beatles)
# sleep(4)
# print("dopo Pete se la svigna pure Stu (non è il mitico Stu che pensate)")
# print("")
# sleep(4)
# print("Formazione :", beatles)
# sleep(3)
# print("1962...")
# sleep(4)
# del beatles[-1]
# print("Rimanenti :", beatles)
# sleep(3)
# print("Arriva Richard Starkey aka Ringo Starr alla batteria")
# beatles.insert(0, "Ringo Starr")
# sleep(5)
# print("--------------------------\n")
# print("| Anno 1962 | the very BEATLES - || the FAB  || formazione finale : \n", beatles)
# print("\n------------------------------------------\n")

# lst.sort()
# print("(.sort method) -- Lista finale ordinata in crescendo : ", lst)
#
# lst.reverse()
# print("(reverse method) -- Lista ordinata dal max al min : ", lst)

###############################   LAB 1


lst = [1, 2, 3, 4, 5]

lst.insert(1, 6)  # [1.6.2,3.4.5]
del lst[0]  # [6,2,3,4,5]
lst.append(1)

print(lst)  # output  :   [6,2,3,4,5,1]

###############################   LAB 2



print("\n-----------  LAB 2  --------------\n")

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for n in lst:
    add = n + 1
    # print("add temp", add)
    lst_2.append(add)
    print(lst_2)  # [2,3,4,5,6]
    print(add)

# output:
#
# [1, 3, 6, 10, 15]
#
# prende
# 1 - -lst[0]
# somma
# a
# 0(sarebbe
# add == 1
# adesso)
# mette in lst_2 >> [1]
#
# add = 1
# --  prende
# 2 - -lst[1]
# somma
# a
# add(2 + 1)
# mettein
# lst_2 >> [1, 3]
#
# add == 3
# prende
# 3 - -lst[2]
# somma
# a
# add(3 + 3)
# mette in lst_2 >> [1, 3, 6]
#
# ..... and so
# on....

###############################   LAB 3


print("\n-------------------------\n")
print("\n-------------------------\n")
print("\n-----------  LAB 3  --------------\n")

ls = [1, [2, 3], 4]

del ls[1]
print("Lunghezza lista aggiornata : ", len(ls))

# output:
#
# Lunghezza
# lista
# aggiornata: 2 << << << <
#
# ls = [1, [2, 3], 4]
# è
# come
# se
# fosse
#
# ls1 = [2, 3]
# ls.insert(1, ls1) >> > lo
# inserisce
# come
# ls[1](fosse
# stato
# 2 >> ls[2])
#
# >> cancella
# ls[1] >> ls = [1, 4]
#
# printa
# length
# di(ls) = 2

##########################################################  LAB 1


print("-------------------------\n")
print("------------LAB 1---------\n")

l = ["D", "h", "F", "c", "A", "Z", "b"]
print("Printa lista", l)

l.sort()
print("Printa lista ordinata : ", l)

# ------------LAB
# 1 - --------
#
# Printa
# lista['D', 'h', 'F', 'c', 'A', 'Z', 'b']
# Printa
# lista
# ordinata: ['A', 'D', 'F', 'Z', 'b', 'c', 'h']

##########################################################  LAB 2


print("-------------------------\n")
print("------------LAB 2---------\n")

a = 3
b = 1
c = 2

l2 = [a, c, b]

l2.sort()
print(l2)  # 1,2,3

# ------------LAB
# 2 - --------
#
# [1, 2, 3]

##########################################################  LAB 3


print("-------------------------\n")
print("------------LAB 3---------\n")

a = "A"
b = "C"
c = "B"
d = " "
e = ""
f = 5
g = "5"
h = 1
k = "1"

l3 = [a, b, c, d, e, f, g, h, k]

l3.reverse()
print("Lista reverse : ", l3)

l3 = [a, b, c, d, f, g, h, k]
# l3.sort()  da errore : o solo <int> o solo <str>

l3 = [a, b, c, d, g, k]
l3.sort()
print("Lista .sort con sole <str>", l3)

l3.reverse()
l3.reverse()
print("Lista 2 reverse method consecutivi : ", l3)  # i 2 .reverse consecutivi si annullano e da l3  (print(l3))

# Solo <str> : sia reverse che sort in presenza di " " lo piazzano all'inizio

# <Stringhe> e #numeri nella stessa lista  : .reverse(method) piazza in mezzo ai numeri (che vengono prima) e stringhe (dopo)
# .sort(method)
# dà
# errore, non
# è
# possibile
# gestire < str > e < int > insieme
#
# ------------LAB
# 3 - --------
#
# Lista
# reverse: ['1', 1, '5', 5, '', ' ', 'B', 'C', 'A']
#
# Lista.sort
# con
# sole < str > [' ', '1', '5', 'A', 'B', 'C']
#
# Lista
# 2
# reverse
# method
# consecutivi: [' ', '1', '5', 'A', 'B', 'C']
# # i 2 .reverse consecutivi si annullano e da l3  (print(l3))
#
# Process
# finished
# with exit code 0

la = [1, 2, 3, 4, 5, 6]

lb = la[1:4]
lc = la[2:-1]
ld = la[-1:]

print("count : ", lb)
print("countc: ", lc)
print("countd: ", ld)

##################################  PROG TROVA DOPPIONI IN UNA LISTA (già lotteria nazionale dio porco)


print("\n*****    Programma LOTTERIA NAZIONALE    *****\n")


l = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# l = [23, 55, 91, 36, 58, 8, 55, 90, 77, 11, 43, 67, 77, 90]
# l = [23, 55, 91, 36, 58, 8, 55, 90, 77, 11, 43]
# l = [1,1,22,333,4444,22,1,5555]

# l = [2,3,5,3,1]
lt = []
lcanc = []
i = 1
max = -9999999
l.sort()

for y in l:
    if y > max: max = y

print("nella lista il numero più grande è >>", max)

for k in l:
    lt.append(k)
    # print("\n-----------------  lt temp", lt, "\n")
    for i in range(len(l) - 1):
        if i == (len(l) - 1): break
        # print("   ***   ***   valore temp i di l", i, "equivale a", l[i], "\n----------------lista l temporanea nel for", l)
        if k == l[i]:
            print("\n!!!!!!    Sto per cancellare", l[i], "dalla lista l   !!!!!! ")
            lcanc.append(l[i])
            print("\n@@@@  Lista numeri cancellati", lcanc, "@@@@\n")
            del l[i]
            print("\nLista temp l DOPO DELETING", l)
            continue

print("\n*************    F I N E     *************************************\n")




print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T    ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")




if (len(l) % 2) != 0:
    lt.sort()
    print("\n >>>>>  LISTONE FINALE :", lt, "<<<<<<")
else:
    lt.append(max)
    lt.sort()
    print(" >>>>>  LISTONE FINALE :", lt, "<<<<<<")

lcanc.sort()
del lcanc[-1]
print("\nLa lista l è stata sminkiata di :", l)

##########################################################  LAB 1
print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T    ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")


print("------------LAB 1---------\n")




l1 = ["A", "B", "C"]

l2 = l1
l3 = l2

del l1[0]
del l1[0]

print(l3)  # 'C'




##########################################################  LAB 2




print("-------------------------\n")
print("------------LAB 2---------\n")



l1 = ["A", "B", "C"]

l2 = l1
l3 = l2

del l1[0]
del l2

print(l3)  # ['B', 'C']

##########################################################  LAB 3


print("-------------------------\n")
print("------------LAB 3---------\n")

l1 = ["A", "B", "C"]

l2 = l1
l3 = l2

del l1[0]
del l2[:]  # cancello il puntamento che è uguale per tutti

print(l3)  # ['A', 'B', 'C']  e invece no : output : []

##########################################################  LAB 4


print("-------------------------\n")
print("------------LAB 4---------\n")

l1 = ["A", "B", "C"]

l2 = l1[:]
l3 = l2[:]  # l3 è una lista uguale a l2 e non vengono eseguite ops quindi rimane uguale

del l1[0]
del l2[0]

print(l3)  # ['A', 'B', 'C']

##########################################################  LAB 5


print("-------------------------\n")
print("------------LAB 5---------\n")

list = [1, 2, "in", True, "ABC"]

print(1 in list)
# True
print("A" not in list)
# True
print(3 not in list)
# True
print(False in list)
# False











####################################################################################



#                          L I S Ts  in Advanced application



####################################################################################



row = []

sq2 = [x**2 for x in range(10)]
print(sq2)

t = [2**i for i in range(8)]
print(t)

odds = [y for y in sq2 if y%2 != 0]
print(odds)



for i in range(8) :
    row.append("WHITE_PAWN")

for k in range(8) :
    row = ["EMPTINESS..." for i in range(8)]
    board.append(row)






