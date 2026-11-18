################################################################################################


#                             GENERATORS  &   CLOSURES


##################################################################################################


#  range() is a generator

# in generale una funzia genera un unico valore  --   un generator



print("\n-------------------   iterator protocol   FIBONACCI  ----------------------------\n")


#  iterator protocol is a way in which an object should behave to conform to the rules imposed by the context of the [ for ] and [ in ] statements.
#  An object conforming to the iterator protocol is called an iterator.



class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn   #   imposta il blocco come arg della class Fib
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1     #    serve da 'counter'
        if self.__i > self.__n:
            print("Stopping iteration...")
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(5):
    print(i, end=" - ")


