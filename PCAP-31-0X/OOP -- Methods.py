########################################

################################################################       OOP methods

###################################





#  >>>>   a method is a function embedded inside a class.


#  >>>>   deve avere almeno 1 parameter





print("\n-------  “ LAB ™ „  --------     3.4.1.1 OOP: Methods  --------------\n")


class Classy:
    def methodman(self):   #  si definisca il method come una func
        print("method")


obj = Classy()   #  si invochi la class come una func() e la si associa ad una var (obj =)
obj.methodman()   #  si richiama il method col name prescelto in fase di compilazione della class stessa






print("\n-------  “ LAB ™ „  --------     3.4.1.1 OOP: Methods  --------------\n")





class Classy1:
    def methodman(self, par):
        print("method:", par)


obj = Classy1()
obj.methodman(1)
obj.methodman(2)
obj.methodman(3)

#  ---output :

# method: 1
# method: 2
# method: 3





print("\n-------  “ LAB ™ „  --------     3.4.1.1 OOP: Methods  --------------\n")






class Classy2:
    varia = 2
    def methodman(self):
        print(self.varia, self.var)   #  self. permette l'accesso alle instance var e class var


obj = Classy2()
obj.var = 3
obj.methodman()

#  ----output :  2  3   >>  methodman richiama varia =2 (class var 'interna')  e var =3  (definito in obj.var = 3)





print("\n-------  “ LAB ™ „  --------     3.4.1.1 OOP: Methods  --------------\n")






class Classy3:
    def other3(self):
        print("other3")

    def methodman(self):
        print("methodman - Classy3")
        self.other3()    #    <<<<  occhio!   qui methodman richiama la def other sopra


obj = Classy3()

obj.methodman()  #  output : methodman - Classy3  (a capo)  other3

print("\nsegue\n")

obj.other3()   #  output : (solo)  other3






print("\n-------  “ LAB ™ „  --------     3.4.1.1 OOP: Methods  --------------\n")





class Classy4:
    def __init__(self, value):  #  definito come method "particolare"
        self.var = value


obj_1 = Classy4("object-classy4-")  #  associa a obj_1 la class inizializzata con func()

print(obj_1.var)   #  richiama la var prescelta (che sarebbe la string "object-classy4-")




print("\n-------  “ LAB ™ „  --------     3.4.1.1 OOP: Methods  --------------\n")




class Classy5:
    def visible(self):
        print("visible")

    def __hidden(self):    #   private method
        print("hidden")


obj = Classy5()
obj.visible()   #  stampa  "visible"

try:
    obj.__hidden()   #  non vede __hidden come method, salta sull'exception
except:
    print("failed")   #  stampa   "failed"

obj._Classy5__hidden()   #  (mangled name)  stampa   "hidden"   beccandola directly dalla class




print("\n-------  “ LAB ™ „  ----class Classy6:----     3.4.1.1 OOP: Methods  --------------\n")



class Classy6:
    def __init__(self, value6 = None):
        self.var6 = value6


obj_16 = Classy6("object")
obj_26 = Classy6()

print(obj_16.var6)   #  stampa  "object"   richiamo .var6 == value6 == "object"
print(obj_26.var6)   #   stampa  None     richiamo .var6 == value6 == (di default nella class è None)



print("\n-------  “ LAB ™ „  ----class Classy7:----     3.4.1.1 OOP: Methods  --------------\n")



class Classy7:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj7 = Classy7()

print(obj7.__dict__)  #  output : {'var': 2}  crea con gli unici valori che ha ([self.]var = 2)

print(Classy7.__dict__)  #  con __dict__ vede solo la class variable  (varia = 1)
# --output : {'__module__': '__main__', '__firstlineno__': 148, 'varia': 1, '__init__': <function Classy7.__init__ at 0x000001F15984B6A0>, 'method': <function Classy7.method at 0x000001F15984B740>, '_Classy7__hidden': <function Classy7.__hidden at 0x000001F15984B7E0>, '__static_attributes__': ('var',), '__dict__': <attribute '__dict__' of 'Classy7' objects>, '__weakref__': <attribute '__weakref__' of 'Classy7' objects>, '__doc__': None}


print("\n-------  “ LAB ™ „  ----Classy8.__name__----     3.4.1.1 OOP: Methods  --------- + type() -----\n")


#  __name__ definisce una string col nome della class
#  esiste solo all'interno di una class, per estrapolare si usa type()


class Classy8:
    pass


print(Classy8.__name__)  #  class che invoca __name__  OK!

obj8 = Classy8()

print('Definiscion (type) della var obj8 : ', type(obj8))   #  output : '<class '__main__.Classy8'>'
print(type(obj8).__name__)  #  OK! se po' ffà   >>>>   restituisce  'Classy8'



#print("obj.__name__ per cortesia :", obj8.__name__)  # AttributeError: 'Classy8' object has no attribute '__name__'.
                                                     #           ￬￬￬         ￬￬￬          ￬￬￬           ￬￬￬
#  Traceback (most recent call last):
#   File "C:\Users\vince\PycharmProjects\Python-PI--1\PCEP2_Scripts\Essentials 2 - MODULO 3\OOP - Methods.py", line 187, in <module>
#     print("TRY dioporco un obj.__name__ per cortesia :", obj8.__name__)
#                                                          ^^^^^^^^^^^^^
# AttributeError: 'Classy8' object has no attribute '__name__'. Did you mean: '__ne__'?



print("\n-------  “ LAB ™ „  ----Classy9.__module__  ----     3.4.1.1 OOP: Methods  --------------\n")


# __module__ restituisce il file currently in mem caricato  (sarebbe __main__)

class Classy9:
    pass


print(Classy9.__module__)    #  ---output : __main__

obj9 = Classy9()

print(obj9.__module__)    #  ---output : __main__




print("\n-------  “ LAB ™ „  ----   3.4.1.1 OOP: Methods  ------  __bases__  --------\n")


#  __bases__  >>>  usato come method rivela le superclass (della relativa class)
#  può avere anche pedice >> |class Sub(SuperOne, SuperTwo)|  -->  Sub.__bases__[0] == SuperOne
#                                                                                                      -->  Sub.__bases__[1] == SuperTwo


class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)  #  ---output :  ( object )   Python class predefinita (in class SuperOne: non c'è nulla)

printBases(SuperTwo)  #  ---output :  ( object )   Python class predefinita (in class SuperTwo: non c'è nulla)

printBases(Sub)       #  ---output :  ( SuperOne SuperTwo )   >>>  tenere presente class Sub(SuperOne, SuperTwo):


print("\n-------  “ LAB ™ „  ----   3.4.1.1 OOP: Methods  --------------\n")


class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(objx):
    for name in objx.__dict__.keys():  #    <<<<<<<  loop sulle keys del __dict__
        if name.startswith('i'):
            val = getattr(objx, name)   #  getattr() becca la key (per intenderci la ricerca iterativa è sulle keys)
            print('Attribute intercettato : ', val)
            print(f"Name preso da if : ", name)
            if isinstance(val, int):  # isinstance > controllo sulla func getattr, 'val' deve essere integer
                setattr(objx, name, val + 1)  #  setattr si riferisce alle keys (for name in objx.__dict__.keys():)


print('echo prima della invocazione : ', obj.__dict__)

incIntsI(obj)
print('echo post invocazione : ', obj.__dict__)





print("\n-------  3.4.1.11 SECTION SUMMARY   --esercizio 1  --------------")

class Snake:
    def __init__(self):
        self.victims = 0

    def increment(self):
        self.victims += 1



print("\n-------  3.4.1.11 SECTION SUMMARY   --esercizio 2  --------------")
print("\n***** Redefine the Snake class constructor so that is has a parameter "
      "\n      to initialize the victims field with a value passed to the object during construction.")

class Snake2:
    def __init__(self, victims):  #  value passed to the object during construction (victims)
        self.victims = victims   #  associazione

    def increment(self):
        self.victims += 1



print("\n-------  3.4.1.11 SECTION SUMMARY   --esercizio 3  --------------")



class Snake3:
    pass

class Hisssss: pass


class Python7(Snake3, Hisssss):
    pass


print(Python7.__name__, 'is a', Snake.__name__, '\n')  # Phython7 is a Snake3
print(Python7.__bases__[0].__name__, 'can be a', Python7.__name__, '\n')  # Snake3 can be a Phython7
print(Python7.__bases__[1].__name__, ' tells the ', Python7.__name__)  # Hisss tells the Phython7



# print("\n¨¨¨¨¨¨☥¨¨¨¨¨¨  ❖--- Ł å ꞵ ® ---❖  ¨¨¨¨¨¨ 3.4.1.12 The Timer class  ¨¨¨¨¨¨\n")
#
#
#
# class Timer:
#     def __init__(self, hh, mm, ss):
#         self.__hh = hh
#         self.__mm = mm
#         self.__ss = ss
#
#     def __str__(self):
#         if self.__hh <= 9 :
#             hx1 = str(self.__hh)
#             self.__hh = f"0{hx1}"
#
#         if self.__mm <= 9 :
#             mx1 = str(self.__mm)
#             self.__mm = f"0{mx1}"
#
#         if self.__ss <= 9 :
#             sx1 = str(self.__ss)
#             self.__ss = f"0{sx1}"
#
#         return f"{self.__hh}:{self.__mm}:{self.__ss}\n"
#
#     def next_second(self):
#         self.__ss = int(self.__ss)
#         self.__mm = int(self.__mm)
#         self.__hh = int(self.__hh)
#
#         if self.__ss == 59 :
#             self.__ss = 0
#
#             if self.__mm == 59:
#                 self.__mm = 0
#
#                 if self.__hh == 23:
#                     self.__hh = 0
#                     self.__hh.__str__()
#                 else: self.__hh += 1
#
#                 self.__mm.__str__()
#             else: self.__mm += 1
#         else:  self.__ss += 1
#
#     def prev_second(self):
#         self.__ss = int(self.__ss)
#         self.__mm = int(self.__mm)
#         self.__hh = int(self.__hh)
#
#         if self.__ss == 0:
#             self.__ss = 59
#
#             if self.__mm == 0:
#                 self.__mm = 59
#
#                 if self.__hh == 0:
#                     self.__hh = 23
#                     self.__hh.__str__()
#                 else:
#                     self.__hh -= 1
#
#                 self.__mm.__str__()
#             else:
#                 self.__mm -= 1
#         else:
#             self.__ss -= 1
#
#
# timer = Timer(23, 59, 59)
# print(timer)
#
# timer.next_second()
# print(timer)
#
# timer.prev_second()
# print(timer)





print("\n¨¨  --- Ł å ꞵ ® ---  ¨¨¨¨¨¨ 3.4.1.13 LAB: Days of the week + WeekDayError(Exception) ¨¨¨¨¨¨\n")



class WeekDayError(Exception):
    pass


class Weeker:
    #week = {'Mon' : 1, 'Tue' : 2, 'Wed' : 3, 'Thu' : 4, 'Fri' : 5, 'Sat' : 6, 'Sun' : 7}
    lst_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        self.__gg = day
        if self.__gg not in Weeker.lst_week: raise WeekDayError  #  piazzando in una delle daf non lo becca
        self.__list = Weeker.lst_week

    def __str__(self):
        return self.__gg

    def add_days(self, n):
         while True :
            if n >= 7 :
                n -= 7
                continue
            else:
                self.__gg = self.__list[n]  #  ritorna in __str__
                return

    def subtract_days(self, n):
         while True :
            if n >= 7 :
                n -= 7
                continue
            else:
                self.__gg = self.__list[-n+1]  #  ritorna in __str__
                return


try:
    weekday = Weeker('Mon')
    print(">>> print codice cmd fouri class : ",weekday)

    weekday.add_days(15)
    print(" + print weekday.add_days(15) : ", weekday)

    weekday.subtract_days(23)
    print(" - print weekday.subtract_days(23) : ", weekday)

    weekday = Weeker('Monday')
except WeekDayError: print("Sorry, I can't serve your request.")





print("\n¨¨¨¨¨¨¨¨¨¨¨  --- Ł å ꞵ ® ---  ¨¨¨¨¨¨ 3.4.1.14 Points on a plane ¨¨¨¨¨¨\n")


# from math import hypot
#
#
# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.x = x
#         self.y = y
#
#     def getx(self):
#         return float(self.x)
#
#     def gety(self):
#         return float(self.y)
#
#     def distance_from_xy(self, x, y):  #  distanza di un 3° punto da x(0,0) e y(1,1)
#         x = Point.getx(self)
#         y = Point.gety(self)
#         distance_xy = hypot(x, y)
#         return distance_xy
#
#
#     def distance_from_point(self, point):
#         distance_fp = hypot(point.getx(), point.gety())
#         return distance_fp
#
#
# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print("point1.distance_from_point(point2) = ", point1.distance_from_point(point2))
# print('point2.distance_from_xy(2, 0) = ', point2.distance_from_xy(2, 0))




print("\n¨¨¨¨¨¨¨¨¨¨¨  --- Ł å ꞵ ® ---  ¨¨¨¨¨¨ 3.4.1.15 Triangle ¨¨¨¨¨¨\n")



from math import hypot


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def getx(self):
        return float(self.x)

    def gety(self):
        return float(self.y)

    def distance_from_xy(self, x, y):  #  distanza di un 3° punto da x(0,0) e y(1,1)
        x = Point.getx(self)
        y = Point.gety(self)
        distance_xy = hypot(x, y)
        return distance_xy


    def distance_from_point(self, point):
        distance_fp = hypot(point.getx(), point.gety())
        return distance_fp



class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__v1 = vertice1
        self.__v2 = vertice2
        self.__v3 = vertice3
        self.__list = [self.__v1, self.__v2, self.__v3]
        self.__lato1 = Point.distance_from_point(self.__v1, self.__v2)
        self.__lato2 = Point.distance_from_point(self.__v1, self.__v3)
        self.__lato3 = hypot(self.__lato1, self.__lato2)

    def perimeter(self):
        __prm = (self.__lato1 + self.__lato2 + self.__lato3)
        return __prm


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
p1 = Point(0, 0)
p2 = Point(1, 0)
p3 = Point(0, 1)
print("distanza v1 - v2 = ", p1.distance_from_point(p2))
print("distanza v1 - v3 = ", p1.distance_from_point(p3))
print("distanza v2 - v3 = ", p2.distance_from_xy(0,1))
print("\nPerimetro = ", triangle.perimeter())

