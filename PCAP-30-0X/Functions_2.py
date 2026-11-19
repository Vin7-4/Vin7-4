#################  2   ########################  2   ############################  2   ###############


#                    F U N C T I O N    2


################  2   ########################  2   #############################  2   ###############




print("ↂ----------2----------    FUNCTIONs  #2  -----------------2--------ↂ\n")



#  *args  e  *kwargs  se non si conosce il numero di vars



def hello(*args):
    for arg in args:  print("Hello", arg,"!")

hello('Peppe', 'Filippo')

#  output :
# Hello Peppe !
# Hello Filippo !





print("ↂ----------2----------    FUNCTIONs  #2  -----------------2--------ↂ\n")




def hello(**kwargs):
    for key, value in kwargs.items():  print("Hello", value,"!")  #  i valori cambiano  >>  for key, value
                                                                  #                     >>  in   kwargs.items():
hello(kwarg1='Caleb', kwarg2='Sydney', kwarg3='Savannah')


# output :
# Hello Caleb !
# Hello Sydney !
# Hello Savannah !





print("\nↂ----------2----------    FUNCTIONs  #2  -----------------2--------ↂ\n")


import math

j = 0

for name in dir(math):
    print(name, end="\t")






print("\nↂ----------2----------    FUNCTIONs  #2  -----------------2--------ↂ\n")



x1 = math.sqrt(4)  #  rad qaud restituisce float

print(f"\nrad quad : {x1}")


































