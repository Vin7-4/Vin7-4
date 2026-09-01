############################################################################################


########   OOP    Generators and closures

# +++   yield   (freeze var del loop)


############################################################################################


class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)

print("\n---------  Mod IV  --  Generators  ------ ###--------")


class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter Fibonacci")
        return self.__iter


object = Class(8)

for i in object:
    print(i)

print("\n---------  Mod IV  --  Generators  ###    The yield statement   ###--------")
print("\n---------               freezing delle vars del loop         ###--------\n")


def fun(n):
    for i in range(n):
        yield i


print(fun(5))  # ---output : <generator object fun at 0x00000208E9D1A9B0>

#  >>>>  si add un loop sulla function

print("\n---------  Mod IV  ###    The yield statement   ###----  add un loop alla def fun(n):----\n")

print('''def fun(n):
    for i in range(n):
        yield i\n

        for k in fun(6):
            print(k, end=' ')\n''')

for k in fun(6):
    print(k, end=' ')

print("\n---------  Mod IV  ###    The yield statement   ###----  def powers_of_2(n):  ----\n")


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

print("\n---------  Mod IV  ###    The yield statement   ###----  [x for x in powers_of_2(5)]  ----\n")


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [x for x in powers_of_2(5)]  # definisce la list e accorpa tutto nel print sotto
print(t)

#   ---output : [1, 2, 4, 8, 16]


print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫ Mod IV  ###  The yield statement   ###  t = list(powers_of_2  --￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩  ↺▼\n")


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(5))
print('Lista generata [list(powers_of_2(3))] : ', t)  # [1, 2, 4, 8, 16]
print("Type t object : ", type(t))  # <class 'list'>

print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫ Mod IV  ###  The yield statement   ###  def fibonacci  --￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩  ↺▼\n")


def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1  # con yield viene restituito i e NON esce dalla def
        else:
            n = p + pp
            pp, p = p, n
            yield n


fibs = list(fibonacci(10))
print(fibs)  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫   Mod IV  Generators and closures  Compactness and elegance  --￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩  ↺▼\n")

list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print('Loop for -- list_1.append(10 ** ex) : ', list_1)  # [1, 10, 100, 1000, 10000, 100000]
print('[10 ** ex for ex in range(6)] : ', list_2)  # [1, 10, 100, 1000, 10000, 100000]

print(
    "\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  (1 if x % 2 == 0 else 0) Compactness and elegance ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print('list.append(1 if x % 2 == 0 else 0) : ', the_list)

print("\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  ### define list or generator ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

the_list10 = [1 if x % 2 == 0 else 0 for x in range(10)]  # lista = obj esistente (len(lista) = True)

the_generator10 = (1 if x % 2 == 0 else 0 for x in range(10))  # generator = serie di valori che si susseguono
# len(generator) = TypeError


for v in the_list10:
    print(v, end=" ")
print()

for v in the_generator10:
    print(v, end=" ")
print()

print('\nlen(the_list10)  :  ', len(the_list10))  # len(the_list10)  :   10

# print('len(the_generator10)  :  ', len(the_generator10))  #  TypeError: object of type 'generator' has no len()


print("\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  ### define list or generator ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)

print("\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  ###   lambda   ### ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print("   ▲￫￫￫￫￫￫￫￫￫￫￫￫   ######           lambda parameters: expression  ￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▲\n")

#  lambda parameters: expression  >>>  per la serie we don't want to hardcode
#                   ￪  ➬ : può essere (math)interpretato come >> tale che [parameter] sia [expression] + ,[eventuale fun]


two = lambda: 2  # resituisce 2
sqr = lambda x: x * x  # resituisce x * x
pwr = lambda x, y: x ** y  # resituisce x elevato a y

for a in range(-2, 3):
    print(f"{a} per sè stesso = ", sqr(a), end="  |||  ")
    print(f"{a} elevato a sè stesso = ", pwr(a, two()))

print("\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  ###   lambda   ### ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")


def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')


def poly(x):
    return 2 * x ** 2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)

#  ---output  :
# f(-2)=18
# f(-1)=8
# f(0)=2
# f(1)=0
# f(2)=2

print("\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  ###   def(poly) = lambda:   ### ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

#  >>>  tenedo presente la def print_function(args, fun): sopra


print_function([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)

print("\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  ###   map() function  ### ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")
print("\n▼↻  ￫￫￫￫￫￫ Mod IV     #####     map(function, list)  ###   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

#  map(function, list)


list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

#  ----------------------------------------------- fyi
lst1 = [map(lambda x: 2 ** x, list_1)]
print('\nlst1 : ', lst1)  # ---output =     lst1 :  [<map object at 0x000001DEF56689D0>]
# --------------------------------------------------------------------------------


print("\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  ###   filter() function  ### ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

from random import seed, randint

seed()  # print numero a casaccio

data = [randint(-10, 10) for x in range(5)]  # randint(-10,10)  >> numero a casaccio in range(10,10)

filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)  # dà una lista
print(filtered)  # presente list([code])  >> dà una lista con elem filtrati

#  ---output :
# [-10, 1, 3, -7, 2]
# [2]   <<<<  vengono filtrati i numeri della list sopra a caso, qui potrebbe essere anche []
#         ovviamente gli altri vengono droppati


######################################


########################################################################   CLOSURES


# >> > tecnica
# che
# permette
# di
# memorizzare
# i
# valori
# nonostante
# il
# contesto in cui
# sono
# stati
# creati
# non
# esista
# più << << <<

######################################


print("\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  ###   CLOSURES  ### ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼")
print("  -------  tecnica che permette di memorizzare i valori nonostante\n"
      "  -------     il contesto in cui sono stati creati non esista più\n")


def outer(par):
    loc = par

    def inner():
        return loc

    return inner


var = 1
fun_out = outer(var)  # con questa invocation si genera la closure
print(fun_out())  # <<<<< anche qui abbiamo una closure

print("\n▼↻  ￫￫￫￫￫￫ Mod IV  Generators and closures  ###   CLOSURES  ### ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")


def make_closure(par):
    loc = par

    def power2(p):
        return p ** loc

    return power2


fsqr = make_closure(2)  # <<<<< qui abbiamo una closure
fcub = make_closure(3)  # <<<<< qui abbiamo una closure

#   una volta agganciata la def make_closure ad una var, le stesse possono essere utilizzate su più fronti

for i in range(5):
    print(i, fsqr(i), fcub(i))  # serie di closure con parameter che cambiano ad ogni loop

# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64


print("\n---------  OOP mod 4  --  4.1.1.15 SECTION SUMMARY  __iter__ + __next__  ###  esrcz 1 ### --------\n")


class Vowels:
    def __init__(self):
        self.vow = "aeiouy "
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]


vowels = Vowels()
for v in vowels:
    print(v, end=' ')  # 'a e i o u y  ' sotto code in aggiunta per experiments
    if v != ' ':
        print('Len di v = ', len(v))
    else:
        print('Len di v = [|space char|] : ', len(v))

print("\n---------  OOP mod 4  --  4.1.1.15 SECTION SUMMARY  ++ lambda & map() ###   esrcz 2 ### --------\n")

#  add codice a even_list = <codice_py> con lambda e map() >>>  output finale deve essere : [1 3 3 5]


#  Traccia : Write a lambda function, setting the least significant bit of its integer argument,
#            and apply it to the map() function to produce the string 1 3 3 5 on the console.


#  Morale della favola : con lambda n: n | 1 si setta l'ultimo bit a 1 solo se è 0


any_list = [1, 2, 3, 4]
even_list = list(map(lambda j: j + 1 if j % 2 == 0 else j, any_list))  # soluzione mia
print('Val con map(lambda j: j+1 if j%2==0 else j, any_list) : ', even_list)

even_list2 = list(map(lambda n: n | 1, any_list))  # soluzione lab corso online pyInstitute
print('\n(Soluzione PyInstitute)--- Val con map(lambda n: n | 1, any_list) : ', even_list2)
#  Morale della favola : con lambda n: n | 1 si setta l'ultimo bit a 1 solo se è 0


######################################################################  experiment


even_list3 = list(map(lambda n: n | 2, any_list))
print('\nVal con map(lambda n: n | 2, any_list) : ', even_list3)

#  Morale della favola : con lambda n: n | 1 si setta l'ultimo bit a 1 solo se è 0


print("\n---------  OOP mod 4  --  4.1.1.15 SECTION SUMMARY  ###  esrcz 3 ###  --------\n")


def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)

    return new_replacement


stars = replace_spaces()
print(stars("And Now for Something Completely Different"))  # And Now for Something Completely Different












































