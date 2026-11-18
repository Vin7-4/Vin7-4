####################################################################################


#      Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж Ж        F U N C T I O N


####################################################################################


print("--------------------FUNCTIONs-------------------------\n")


def message():
    print("Diahane")
    print("fine fanx~cion")


print("Starte")
message()  # JUMPA NELLA DEF
print("Endit")
message()  # arijampa nella def

# def reload() :
#     s = True
#     while s:
#
#
#         print("\n EXIT\n")
#         ѯ = input("[s] continua, tasto qualsiasi per uscire ?>_ ")
#         if ѯ == "s" :
#             continue
#         else: exit(0)


print("-------------------------\n")
print("------------LⱯB 1---------\n")

# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())
# message()
# d = int(input())

# print("Somma num immessi : ", a + b + c + d)
# print("\n-------------------------\n")
# reload()

#
# PyDev
# console: starting.
# Python
# 3.12
# .6(tags / v3
# .12
# .6: a4a2d2b, Sep
# 6
# 2024, 20: 11:23) [MSC v.1940 64 bit(AMD64)]
# on
# win32
#
# >> > print(None + 3)
#
# Traceback(most
# recent
# call
# last):
# File
# "<input>", line
# 1, in < module >
# TypeError: unsupported
# operand
# type(s)
# for +: 'NoneType' and 'int'


def multiply(a, b):
    x = a * b
    return #<< < solo
    return # senza var

#>> > print(multiply(3, 4))


#  None     <<<<<< > output sarà " None "


def wish():
    print("Avugurio!")
    return "Ui uisc iu a merri kristmas!"


print("---a seguire output di wish()----------\n")
wish()
print("\n------a seguire output di print(wish())-------\n")
print(wish())

# output:
#
# ---a
# seguire
# output
# di
# wish() - --------- >> > senza
# print
#
# Avugurio!
#
# ------a
# seguire
# output
# di
# print(wish()) - ------  col
# print
# della
# stessa
#
#
# def >>>
#
#
# def wish() >>
#
#     >> print(wish())
#
# Avugurio!
# Ui
# uisc
# iu
# a
# merri
# kristmas

#####################################################################################################################


###################                       Anno bisestitico


#########################################################################################################################



print("\n--------------Anno bisestile-----------\n")


# y4= y%4   #common
# y100=y%100 #leap
# y400=y%400  #common
# otherwise is leap

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def test_bisstl(test_data=None):
    test_data = [1900, 2000, 2016, 1987, 1700]
    print("----- Sequenza di test\n(TEST) Lista anni : ", test_data)
    test_result = [False, True, True, False, False]

    print("(TEST) segue DATA per confronto\n -----(in sequenza lista data - )\n"
          "   ****   INFO   ****\nTrue -> Bisestile\nFalse -> NON è bisestile\n", test_result,
          "\n------------------------\n")

    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr, "-> ", end="")
        result = is_year_leap(yr)
        if test_result[i]:
            print("OK è bisestile!")
        else:
            print("Nope... non è bisestile...")
    return result


u = True

while u:
    x = int(input("Inserisci anno ?>_ "))
    # if ValueError is False: #  << << << << << << << << << << > exception try except (ValueError)
    #  print("Non hai inserito nessun dato...")
    #  continue
    # else:
    p = is_year_leap(x)
    z = test_bisstl()
    print("Test anno inserito :", p)
    print("\n---  TEST (anno di riferimento)\n", z, "\n-----------\n")
    print("L'anno prescelto (", x, ")", end="")
    if p: print(" è bisestile\n")
    else: print(" non è bisestile\n")
    u = input("s per continuare / tasto qualsiasi per uscire -?[<INVIO> esce subito]>_ ")
    if u == "s": continue
    else: exit(0)


################################# sì prova a day in the air.....  prog totale (bisestile , mese , day della semana)
##################################  corrisponde a FUNCTIONS 2.py


###################  e funge pure!


from calendar import month
from time import sleep


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


############################################################  TESTING YEAR


def test_bisstl(test_data=None):
    test_data = [1900, 2000, 2016, 1987, 1700]
    print("----- Sequenza di test\n(TEST) Lista anni : ", test_data)
    test_result = [False, True, True, False, False]

    print("(TEST) segue DATA per confronto\n -----(in sequenza lista data - )\n"
          "   ****   INFO   ****\nTrue -> Bisestile\nFalse -> NON è bisestile\n", test_result,
          "\n------------------------\n")

    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr, "-> ", end="")
        result = is_year_leap(yr)
        if test_result[i]:
            print("OK è bisestile!")
        else:
            print("Nope... non è bisestile...")
    return result


def days_in_month(month, year):
    yr = is_year_leap(year)
    dmx = ["Month0-nodays", "31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
    dym = ["Month-NO", "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio",
           "Giugno", "Luglio", "Agoglio", "Settembre", "Ottembre",
           "Novembre", "Diciassembre", " - NoMonth - "]

    if month > 13:
        print("Mese non valido... DEVE essere compreso tra 1 e 12")
        month = str(None)
        print(month, "exit")
        exit(0)

    if yr:
        print("L'anno prescelto (", year, ") è bisestitico e ", end="")
        for i in range(0, len(dmx)):
            if i == month:
                print("il mese prescelto (" + str(dym[i]) + ") sarà composto da", (int(dmx[i]) + 1), "giorni.")
            else:
                continue
            return
    else:
        print("L'anno NON è bisestitico e il ", end="")
        for i in range(0, len(dmx)):
            if i == month:
                print("il mese prescelto sarà composto da", dmx[i], "giorni.")
            else:
                continue
            return


################################################  A DAY IN THE AIR.....  CONTINUA.....


def a_day_in_the_air(gg, month, year):
    ld = ["- NO-day[0] -", "Lunerdì", "Marterdì", "Mercolerdì", "Gioverdì",
          "Venerdì", "Sabbato", "Dimanches de les Comanchis", "JumpBack"]
    lset = ["0-day", 1, 2, 3, 4, 5, 6, 7, "No-day"]
    ldm = ["Month0-nodays", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, "Jump", "JumpMon"]
    gg

    is_year_leap(year)
    days_in_month(month, year)

    for i in range(1, 7):
        while gg > 7:
            gg = gg - 7
            if gg < 7:
                print("Il giorno prescelto corrisponderà a", ld[gg])
                break
            if gg == 7:
                print("Il giorno", gg, "corrisponderà a", ld[gg])
                break

        return "\n--------------"


d = int(input("Immetti giorno del mese (num corrispondente) ?>_ "))
n = int(input("Immetti mese (num corrispondente) ?>_ "))
ann = int(input("Immetti annualità ?>_ "))

v = a_day_in_the_air(d, n, ann)

print(v)


# while True:
#     d = int(input("Immetti giorno del mese (num corrispondente) ?>_ "))
#     n = int(input("Immetti mese (num corrispondente) ?>_ "))
#     y = int(input("Immetti anno ?>_ "))
#     days_in_month(y,n)
#     print("\n.........F I N E.............\n")
#
#     è = input("' s ' per continuare, <[ ENTER ]> per uscire : ?>_ ")
#     if è == "s":
#         continue
#     else:
#         exit(0)


#########################################  lista numeri primi

######################################################################  test ---da rivedere


def is_prime():
    k = 1
    lst = [2, 3]
    for num in range(3, 20, 2):
        if num == 3: continue
        if num % 3 != 0:
            print("Beccato", num, "(hit #)" + str(k))
            lst.append(num)
            print("Lista temp al numero :", num, "sarebbe >>", lst, "in posizione", k)
            k += 1
    print("\n---------\nLista finale di numeri primi nel range 0 >>", lst[-1], "sarà =", lst)


#########################################################################################################


#################  prog che funzia


######################################  OPTIMUS PRIME numbers


def is_prime(num):
    if num % 2 == 0:
        num = False
    elif num % 3 == 0:
        num = False
    else:
        num = True
    return num


n = int(input("Inserisci numero# ?>_ "))
p = is_prime(n)
print(test_prime([n]))
if p:
    print("\n----------\nIl numero", n, "è PRIMO")
else:
    print("\n----------\nIl numero", n, "NON è un numero primo...")

while True:
    n = int(input("Inserisci numero# ?>_ "))
    p = is_prime(n)
    print(test_prime([n]))
    if p:
        print("\n----------\nIl numero", n, "è PRIMO")
    else:
        print("\n----------\nIl numero", n, "NON è un numero primo...")

    è = input("s per continuare -- tasto qualsiasi per uscire : ?>_ ")
    if è == "s":
        continue
    else:
        exit(0)




#########################################################




############################################    CONVERSIONE DI LITRI/KM  IN MILES per GALLON


# 1 usa mile = 1609.344 metri = 1.609344km
# 1 mile = 1,609344km
# 1 km = 0.621371192237334 miles
# 100 km = 62.13711922373339 mils
# 100 miles = 160,9344km
# 1 gallone = 3.785411784 litri

def liters_100km_to_miles_gallon(lts):
    gal = 3.785411784
    km_miles = 100 / 1.609344  # 62.13711922373339

    lgal = (lts / gal)  # 1.0302710041967789
    lts = float(km_miles / lgal)
    return lts


def miles_gallon_to_liters_100km(miles):
    mls_km100 = 62.13711922373339  # 100km sarebbero 62.13711922373339 miglia  (è 100/1.609344)

    gal = 0.26417205235814845  # rapporto l/gal sarebbe 1/3.785411784
    delta = (mls_km100 / gal)
    miles = (delta / miles)
    return miles


while True:
    x = float(input("Inserisci litri : ?>_ "))
    y = float(input("Inserisci miglia (o miles if u prefer) : ?>_ "))
    print("Litri/100km su miles per gallons : ", liters_100km_to_miles_gallon(x))
    print("Miles per gallons su l ogni 100km : ", miles_gallon_to_liters_100km(y))

    è = input("\n\1>>> Vuoi continuare? <<<\1\n{ s per continuare -- [ENTER] per uscire } ?>_ ")
    if è == "s":
        continue
    else:
        exit(0)




############################################    PROG SCELTA + VARIE




# 1 usa mile = 1609.344 metri = 1.609344km
# 1 mile = 1,609344km
# 1 km = 0.621371192237334 miles
# 100 km = 62.13711922373339 mils
# 100 miles = 160,9344km
# 1 gallone = 3.785411784 litri

def conv_km_in_miles(km):
    km = km / 1.609344
    return km


def conv_miles_in_km(mls):
    mls = mls * 1.609344
    return mls


def liters_100km_to_miles_gallon(lts):
    gal = 3.785411784
    km_miles = 100 / 1.609344  # 62.13711922373339

    lgal = (lts / gal)  # 1.0302710041967789
    lts = float(km_miles / lgal)
    return lts


def miles_gallon_to_liters_100km(miles):
    mls_km100 = 62.13711922373339  # 100km sarebbero 62.13711922373339 miglia  (è 100/1.609344)

    gal = 0.26417205235814845  # rapporto l/gal sarebbe 1/3.785411784
    delta = (mls_km100 / gal)
    miles = (delta / miles)
    return miles


while True:
    print("**************   Prog vari  **************\n")
    print("Scegli numero corrispondente : \n\1 1. Conversione km in miles\n"
          "\1 2. Conversione miles in km\n"
          "\1 3. Programma definisci litraggio e miglia medi\n ")
    risp = input("Make ur choice [ 1 , 2 , 3 ] ?>_ ")

    if risp == "1":
        km = int(input("\nProg converti km in miles\nInserisci km(s) da convertire in miles ?>_ "))
        print(conv_km_in_miles(km))

    elif risp == "2":
        mls = int(input("\nProg converti miles in km\nInserisci miglia(s) da convertire in km(s) ?>_ "))
        print(conv_miles_in_km(mls))

    elif risp == "3":
        x = float(input("Inserisci litri : ?>_ "))
        y = float(input("Inserisci miglia (o miles if u prefer) : ?>_ "))
        print("Litri/100km su miles per gallons : ", liters_100km_to_miles_gallon(x))
        print("Miles per gallons su l ogni 100km : ", miles_gallon_to_liters_100km(y))

    else:
        print("\n>>>>>>>>  Hai digitato un carattere non valido!\n"
              "ricarico!\n")
        continue

    è = input("\n\1>>> Vuoi continuare? <<<\1\n{ s per continuare -- [ENTER] per uscire } ?>_ ")
    if è == "s":
        continue
    else:
        exit(0)




###############################################################################


###############################################################################




print("-------------------------\n")
print("------------LAB 1---------\n")


def hi():
    return


print("Hi!")

hi()  # Hi!  (senza None, solo Hi!)

print("-------------------------\n")
print("------------LAB 2---------\n")


def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False


print(is_int(5))
print(is_int(5.0))
print(is_int("5"))  # True  False  None

print("-------------------------\n")
print("------------LAB 3---------\n")


def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst


print(even_num_lst(11))  # [0, 2, 4, 6, 8 ,10]

print("-------------------------\n")
print("------------LAB 4---------\n")


def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list


foo = [1, 2, 3, 4, 5]
print(list_updater(foo))  # [1, 4, 9, 16, 25]

#
# def hi():
#     return << << < esce
#     col
#     'return'
#     e
#     NON
#     esegue
#     più
#     nulla!
#     print("Hi!")


hi()  # output : None

print('\n-------    ￬￬￬￬  ￬￬￬￬   ￬￬￬￬  NUMERI PRIMI  ￬￬￬￬    ￬￬￬￬    ￬￬￬￬    ---------------\n')


def is_prime(num):
    k = 0
    for x in range(1, 1000):
        if num % x == 0: k += 1
    if k == 2: return num


for i in range(1, 90):
    if is_prime(i + 1): print(i + 1, end=" ")

print('\n-------    ￬￬￬￬  ￬￬￬￬   ￬￬￬￬   ￬￬￬￬    ￬￬￬￬    ￬￬￬￬    ---------------\n')


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


# my_list_2 = [2, 3] << << stesso
# nome
# nella
# func
#
#
# def my_function
#     my_function(my_list_2)


print("Print #5:", my_list_2)

# output:
#
# Print  # 1: [2, 3]
# Print  # 2: [2, 3]
# Print  # 3: [0, 1]
# Print  # 4: [2, 3]
# Print  # 5: [2, 3]

# >> >> > Cambiando my_list_2 in my_list_3


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)# << << qui
    #                                         sottolinea in rosso
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2) #<< << qui
    #                                         sottolinea in rosso


# my_list_3 = [2, 3] << << my_list_3
# NON
# è
# presente
# nella
# func #
# def my_function
#     my_function(my_list_3)


print("Print #5:", my_list_3)

# output:
#
# Print  # 1: [2, 3]
#
# e in aggiunta  ￬￬￬￬￬
#
# Traceback(most
# recent
# call
# last):
#
# File
# "main.py", line
# 10, in < module >
#
# my_function(my_list_3)
#
# File
# "main.py", line
# 3, in my_function
#
# print("Print #2:", my_list_2)
#
# NameError: name
# 'my_list_2' is not defined

#########################  variabili 'global'  >>  attento alla posizione della variabile !!!


a = 1


def fun():
    global a
    a = 2
    print(a)


fun()
# a = 3 >> > è piazzato DOPO la call della fgunzia print(a)

# output:
#
# 2
# 3

a = 1


def fun():
    global a
    a = 2
    print(a)


a = 10
fun()
print(a)

print("\n----------------------------------------------\n")

dict1 = {'one': 'two', 'three': 'one', 'two': 'three'}

v = dict1['one']

print(f'V preliminare prima del for >>  {v}')  # two

for k in range(len(dict1)):
    v = dict1[v]
    print(f'\ngiro {k} -- v = {v}')

print('var v dopo il for loop : ', v)

print("\n----------------------------------------------\n")

lst1 = ['mary', 'had', 'a', 'little', 'lamb']


def lst1(lst1):
    del lst1[3]
    lst1[3] = 'ram'


print(lst1(lst1))  # output è nullo, code errato!




















































































