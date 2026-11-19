##########################################################

#                            TEST CODE utile

##############################################################



#  >>>  GUI python

# import tkinter as tk
# from time import sleep
#
# w1 = tk.Tk()
#
#
# w1.geometry("600x200")
# w1.title("Esempio 1 py window tkinter")
#
#
# bt1 = tk.Button(text="Esempio fenetre")
# bt1.grid(row=50, column=50)
#
#
# w1.mainloop()
# sleep(1)
# w1.quit()


print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫------------------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")





# # This code causes the MemoryError exception.
# # Warning: executing this code may affect your OS.
# # Don't run it in production environments!


# string = 'x'
# try:
#     while True:
#         string = string + string
#         print("op al sec : ", len(string))
#         print("/echo-x : ", string)
# except MemoryError:
#     print('This is not funny!')




print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T    ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")


# t1 = "C:\\CPY_SAVES\\Pylog.txt"

str1 = [1,2,3,4]


print('Stringa completa : ', str1)
print('Conteggio presenza numero 2 : ', str1.count(2))
print(str1.count(3))




print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T    ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")



import time

h1 = time.time()

timestamp = 1472569786  # deconversione Unix epoch da totale millisec a data e ora precisi
print(time.ctime(timestamp))

print(f"\ndata, giorno e ora : {time.ctime(h1)}")



print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T    ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")


print('test')



print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T   napalm ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")

# from napalm import get_network_driver
#
# driver = get_network_driver("eos")
# device = driver("192.168.1.98", "username", "password")
# device.open()
# facts = device.get_facts()
# device.close()


print("------------LAB 3---------\n")

l1 = ["A", "B", "C"]

l2 = l1
l3 = l2

print(f"l2 = l1 >> {l2}")   #  ["A", "B", "C"]
print(f"l3 = l2 >> {l3}")   #   ["A", "B", "C"]

del l1[0]

print("----- l1 dopo >del l1[0] : ", l1, end="\n")  #  "B", "C"]
print("----- l2 dopo >del l1[0] : ", l2, end="\n")  #  "B", "C"]

del l2[:]  #

print("l2 dopo >del l2[:] : ", l2, end="\n")

print("lista l3 finale (con l3 = l2): ", l3)  # lista l3 finale :  []

# output :

# l2 = l1 >> ['A', 'B', 'C']
# l3 = l2 >> ['A', 'B', 'C']
# ----- l1 dopo >del l1[0] :  ['B', 'C']
# ----- l2 dopo >del l1[0] :  ['B', 'C']
# l2 dopo >del l2[:] :  []
# lista l3 finale :  []



print("\n------------                  LAB 3                ---------\n")



tup1 = (1., 'c', 77, True)

print(tup1)

print(tup1[3])

# tup1[0] = 15     >>>  TypeError: 'tuple' object does not support item assignment



print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T  assegnazione fast a var  ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")



(a1, b2, c3) = (1, 2, 3)

print(f"\ndata l'ug tra tuples (a1, b2, c3) = (1, 2, 3)\n")

print("a1 = ", a1)
print("c3 = ", c3)



print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T  set   ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")


set1 = {1, 4, "b", False, 'f',5}
set2 = {5, 'f', True, 1, 'b', 7}


print("--  MERGE  :  set1 | set2 = ", set1 | set2)   #   =  {False, 1, 'b', 4, 5, 'f'}   True NON c'è

print("\nIntersection (set2 & set1  --  componenti uguali tra 2 tuples) : ", set2 & set1)  #  {True, 'f', 'b', 5}
print("\nIntersection (set1 & set2  --  componenti uguali tra 2 tuples) : ", set1 & set2)  #  {True, 'f', 'b', 5}


print("\nTrue | False = ", True | False)
print("True & False = ", True & False)




print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T  set   ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")


# while True:
#     string = input('Enter some text to print. \nType "done" to quit>')
#     if string == 'done': break
#     print(string)
#
# print('Done!')



print("\n▼↻------￫￫￫￫￫￫￫￫￫￫￫￫￫---------  T  E  S  T  linkedin game   ---------￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩------↺▼\n")


str1 = "ion"
str2 = "rcne"
str3 = "ypt"

l1 = len(str2) - (len(str2)+1)
st1 = ""

for k in range(l1,-(len(str2)+1),-1):
    st1 += str2[k]

magic_word_is = st1+str3+str1
print(f"(probably)FREE COFFEEEEEEEE!!!!!! >>>FYI the magic word is < {magic_word_is} >")





























