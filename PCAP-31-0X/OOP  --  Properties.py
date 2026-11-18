###########################################################################################################################

########################                          OOP properties

###########################################################################################################################


# -------------------------------------  CLASSE ESEMPIO + names specifici


class Sample:
    gamma = 0     #    << << << < Class variable.

    def __init__(self):
        self.alpha = 1     #  << << << < Instance variable.
        self.__delta = 3     #  << << << < Private instance variable.


obj = Sample()
# obj.beta = 2 << << << < Another instance variable(existing only inside the "obj" instance.) print(obj.__dict__)
#
# ----   output:
#
# {'alpha': 1, '_Sample__delta': 3, 'beta': 2}

print("\n-------  “ LAB ™ „  --------     3.3.1.1 OOP: Properties  --------------\n")


class ExampleClass:
    def __init__(self, val=1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()  # qui val =1
example_object_2 = ExampleClass(2)  # oberct_2 avrà come val >>> def __init__(self, val = 2):

example_object_2.set_second(3)  # object_2 avrà un 2° parameter (=3) che verrà elaborato
# #dalla seconda def della class (def set_second(self, val=3):)

example_object_3 = ExampleClass(4)  # qui val =4
example_object_3.third = 5  # creazione method on the fly
#                  ↸ qui viene creato un method al volo (.third) 'fuori' dalla class  >> val =5

# Python objects, when created, are gifted with a small set of predefined properties and methods.
# Each object has got them, whether you want them or not. One of them is a variable named __dict__ (it's a dictionary).


print(example_object_1.__dict__)  # output :  {'first': 1}

print(example_object_2.__dict__)  # prende val di __init__ =2  >>> example_object_2 = ExampleClass(2)
#                                  val di set_second =3  >>>  example_object_2.set_second(3)   output : {'first': 2, 'second': 3}


print(example_object_3.__dict__)  # val da example_object_3 = ExampleClass(4)
# val =5 da example_object_3.third = 5   >>>>  output : {'first': 4, 'third': 5}


example_object_4 = ExampleClass(4)
example_object_4.set_second(8)
example_object_4.third = 12
example_object_4.fourth = 16

print("\nEsempio di var.[method] on-the-fly : ", example_object_4.__dict__)

print("\n-------  “ LAB ™ „  --------     3.3.1.1 OOP: Properties  ----int e ext private var ----------\n")


class ExampleClass:
    def __init__(self, val=1):
        self.__first = val

    def set_second(self, val=2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

#  output:

# {'_ExampleClass__first': 1}    #  var private (__first) esce come '_ExampleClass__first'
# {'_ExampleClass__first': 2, '_ExampleClass__second': 3}  # __first e __second escono con _ExampleClass
# {'_ExampleClass__first': 4, '__third': 5} # la var __third NON apaartiene al code int della class quindi
# quindi in output avremo '__third' senza '_ExampleClass


print("\n-------  “ LAB ™ „  --------     3.3.1.1 OOP: Properties  ----istanza interna (.counter) ----------\n")


class ExampleClass:
    counter = 0  # class variable, piazzata PRIMA del constructor __init__, può essere comunque utilizzata come istanza interna

    def __init__(self, val=2, val2=4):
        self.__first = val
        self.__sec = val2
        ExampleClass.counter += 1  # <<<  class variable utilizzata come istanza interna (.counter)
        #       presenta lo stesso valore in tutte le istanze


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2, 7)
example_object_3 = ExampleClass(4, 8)

print(example_object_1.__dict__, " >> Counter object 1 = ", example_object_1.counter, '\n')
print(example_object_2.__dict__, " >> Counter object 2 = ", example_object_2.counter, '\n')
print(example_object_3.__dict__, " >> Counter object 3 = ", example_object_3.counter)

#  ---output :  >>>  la class variable counter sarà sempre =3

# {'_ExampleClass__first': 2, '_ExampleClass__second': 4} Counter object 1 =  3

# {'_ExampleClass__first': 2, '_ExampleClass__second': 7} Counter object 2 =  3

# {'_ExampleClass__first': 4, '_ExampleClass__second': 8} Counter object 3 =  3


# print("\n----  “ LAB ™ „  --------  3.3.1.4 OOP: Properties ----class variable (private)----\n")
#
#
# class ExampleClass:
#     __counter = 0  #  class variable
#     def __init__(self, val = 1):
#         print('Nome class : ', ExampleClass.__name__)  #  orpello
#         self.__first = val    #  instance variable
#         ExampleClass.__counter += 1
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)  #  3° chiamata >> counter =3
#
# print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
# print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
# print(example_object_3.__dict__, example_object_3._ExampleClass__counter)
#
#
# #  ----  output :  le var "interne" (dopo __init__) rimangono '_ExampleClass__first'
#
# # {'_ExampleClass__first': 1} 3  #  var __counter rimane invariata nell'echo dell'output
# # {'_ExampleClass__first': 2} 3
# # {'_ExampleClass__first': 4} 3
#
#
#
# print("\n----  “ LAB ™ „  --------  3.3.1.4 OOP: Properties ----class variable = parameter----\n")
#
#
#
# class ExampleClass:
#     varia = 1  #  class variable
#     counter = 0
#     def __init__(self, val):
#         self.varia = val    #  instance variable
#         ExampleClass.varia = val  #  il constructor inizializza la class var col param (interno) val
#         ExampleClass.counter += 1
#
#
# print(ExampleClass.__dict__)    #   <--- output[3]  invocazione pura della class SENZA parameter
# example_object = ExampleClass(2)
# example_object_123 = ExampleClass(7)
#
# print(ExampleClass.__dict__)  #   <--- output[4]
# print(example_object.__dict__)
#
# print("Counter invocazioni del codice = ", example_object.counter)  # le invocazioni della class sono 2
#
#
#
#
# # --- output 1 :   [se presente ''varia = val'' (dopo __init__ del constructor  --->def __init__(self, val):)]
# #   {}   <<<<   __dictionary__ vuoto
#
#
# # --- output 2 :   [se presente ''self.varia = val'' (dopo __init__ constructor  --->def __init__(self, val):))]
# #   {'varia': 2}   <<<<   value:key presenti nel __dictionary__
#
#
#
# #   ----------------------------------- output[3]  invocazione pura della class SENZA parameter
#
# # {'__module__': '__main__', '__firstlineno__': 509, 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x0000016777004CC0>, '__static_attributes__': ('varia',), '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
# #                                                             ↸ >> 'varia': 1
#
#
# #   ----------------------------------- output[4]  invocazione con l'assegnazione >> ''example_object = ExampleClass(2)''
#
# # {'__module__': '__main__', '__firstlineno__': 509, 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x0000016777004CC0>, '__static_attributes__': ('varia',), '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
# #                                                             ↸ >> 'varia': 2
#
#
#
# print("\n----  “ LAB ™ „  --------  3.3.1.6 OOP: Properties ---- only one of two possible attributes ----\n")
#
#
# class ExampleClass1:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object = ExampleClass1(1)
#
# print(example_object.a)
# #print(example_object.b)   #  ERRORE  (AttributeError: 'ExampleClass' object has no attribute 'b')
#
#
# #
# #  1  <  1%2 !=0
#
# # >>>>>    print(example_object.b) darà errore!
#
# #  Traceback (most recent call last):
# #    File "C:\Users\vince\PycharmProjects\Python-PI--1\PCEP2_Scripts\Essentials 2 - MODULO 3\OOP 1.py", line 567, in <module>
# #      print(example_object.b)
# #            ^^^^^^^^^^^^^^^^
# #  AttributeError: 'ExampleClass' object has no attribute 'b'
#
#
#
# print("\n----  “ LAB ™ „  --------  3.3.1.6 OOP: Properties ---- only one of two possible attributes ----")
# print("  >>>>  evitare  AttributeError: : funzia hasattr(example_object, 'b'):\n")
#
#

# >> >> restituisce
# True
# oppure
# False

# class ExampleClassHA1:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object0 = ExampleClassHA1(1)
# print(example_object0.a)
#
# if hasattr(example_object0, 'b'):     #  evita AttributeError: nel caso 'a' esista
#     print("\nCheck esistenza attributo : ")
#     print(example_object0.b)
#
#
#
# print("\n----  “ LAB ™ „  --------  3.3.1.6 OOP: Properties ---- only one of two possible attributes ----")
# print("  >>>>  evitare  AttributeError: >>>>  try:   --------------------\n")
#
#
# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# example_object = ExampleClass(1)
# print(example_object.a)
#
# try:
#     print('- b - :', example_object.b)
# except AttributeError:
#     pass


print("\n----  “ LAB ™ „  --------  3.3.1.6 OOP: Properties ---- only one of two possible attributes ----")


class ExampleClassHA2:
    a = 1  # class variable, può essere richiamata "all'esterno"

    def __init__(self):
        self.b = 2  # instance var NON può essere richiamata dalla class "all'esterno"


example_object = ExampleClassHA2()

print(hasattr(example_object, 'b'))  # True
print(hasattr(example_object, 'a'))  # True
print(hasattr(ExampleClassHA2,
              'b'))  # False   >>  'b' NON può essere richiamata dalla class (non esiste ExampleClassHA2.b)
print(hasattr(ExampleClassHA2, 'a'))  # True   >>  'a' può essere richiamata dalla class (esiste ExampleClassHA2.a)

print("\n----  “ LAB ™ „  --------  3.3.1.8 OOP: Properties ---- only one of two possible attributes ----")


class ExampleClassHA3:
    attr = 1


print(hasattr(ExampleClassHA3, 'attr'))  # True
print(hasattr(ExampleClassHA3, 'prop'))  # False  (non esiste nessuna var con quel name)


class Python:
    population = 1
    victims = 0

    def __init__(self):
        self.length_ft = 3
        self.__venomous = False


print("\n-------  “ LAB ™ „  --------    3.3.1.9 SECTION SUMMARY  --------------\n")


# print("\n-------  con code copiato da corso (previstissimo)  --------------\n")


class Python1:
    population = 1
    victims = 0

    def __init__(self):
        self.length_ft = 3
        self.__venomous = False


version_2 = Python1()

#
print("\n-------  3.3.1.9 SECTION SUMMARY   --esercizio 2  --------------")
print("-------  3.3.1.9 SECTION SUMMARY   --negazione della property __venomous  --------------\n")

version_2._Python1__venomous = not version_2._Python1__venomous  # mangled name

print("\n-------  3.3.1.9 SECTION SUMMARY   --esercizio 3  esistenza attributo  constrictor --------------\n")

print(hasattr(version_2, 'constrictor'))  # False
