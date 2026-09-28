####################################################################################


##########################   LOGIC & BIT OPERATIONS


# file
# OP
# SU
# OPERATORI.txt
# ci
# va
# di
# sintesi
# veloce

####################################################################################


# NON SI UTILIZZANO floats


# condizioni equivalenti

var = 10

print(var > 0)  # True
print(not (var <= 0))  # True

################ Leggi di De Morgan

# la negazione di una congiunzione è la disgiunzione delle negazioni
# la negazione di una disgiunzione è la congiunzione delle negazioni

p = 0
q = 1

print(not (p and q) == (not p) or (not q))

print(not (p or q) == (not p) and (not q))

#########################


x = 1

j = not not x  # equivale a dire j = x

#####################   Bitwise operators


#  !!!!!   tra l'op logica e quella bitwise il risultato è differente

# & (ampersand) > congiunzione bitwise  (sarebbe 'and')

# | (bar) > disgiunzione bitwise    (sarebbe 'or')

# ~ (tilde, Alt-sx+126) > negazione bitwise   (sarebbe 'not')

# ^ (caret) > bitwise exclusive (sarebbe 'xor')


############################ diff tra op logica e op bitwise


i = 15

j = 22

# (bin)i = 00000000000000000000000000001111

# (bin)j = 00000000000000000000000000010110


### op logica

log = i and j  # rappresenta :True perchè soddisfa la condizione dell'and  (uno dei due arg deve essere non-zero)

bit = i & j  # &=congiunzione >>
# op logica > log(neg) = not i |:False|

bitneg = ~i

print(~i)  # output -16

######################   deal with single bits


m = 8

mnot = ~m

#####################################   Binary shift ( a  dx |>>|  oppure  sx |<<| )


print("\n-------------------------\n")
print("\n-------------------------\n")
print("\n-------------------------\n")

v = 17

vdx = v >> x     #  >> > calcola
# v // (2 elevato a x)
#
vsx = v << y #>> > calcola
# v * (2 elevato a y)
#


print(v, vsx, vdx, sep="\n" * 2)
#
# #  output  >>>
# (v >> 1) - -- 8 >> sarebbe
# 17 // (2 elevato a 1) >> 17 * 2
# (v << 2) - -- 68 >> sarebbe
# 17 * (2 elevato a 2) >> 17 * 4(shiftare
# di
# 2
# bit
# equivale
# alla
# var * 4)










######################################   test1


x = 1
y = 0

z = ((x == y) and (x == y)) or not (x == y) #>> > (False and False) = False or not (False) = True >> > False or True >> > True

print(not (z))

print(not (True)) #>> > False




#-------------------------------------------------------------------   Expl




z = ((x == y) and (x == y)) or not (x == y)

#  1==0 > False(=0)         or  not(False) = True
#  1==0 and 1==0 > False(=0)

# il tutto si riduce a :  False  or  True   >>>  quindi è True  >>>  z = True

print(not (z))
# printa not(True)  >>>  False  (=0)





#----------------------




z = ((x == y) and (x == y)) or not (x == y)

print(not (z))

# output :  False


######################################   test 2


x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print("a = x & y", a, "b = x | y", b, "c = ~c", c, "d = x ^ 5", d, "e = x >> 2", e, "f = x << 2", f,
           sep="   --   ", end="")

# output:
#
# a = x & y - -   0 - -        confronto(binary)
# tra
# 4(x=0100)
# e
# 1(y=0001)
# esce
# 0000( = 0)



b = x | y #- -   5 - -            confronto a
# sovrascrittura(tenendo
# presente
# la
# " | ", 1
# prevale
# su
# 0 = 1 )
# 4(x=0100)
# e
# 1(y=0001)
# esce
# 0101( = 5)

# 0
# 1
# 0
# 0
# 0
# 1
# 0
# 0
# 0
# 0
# 0
# 1
# ----------
# 0
# 1
# 0
# 1

c = ~x #- -   -5 - -        ribalta
# numero
# ~4 >> 4(bin) = 0100 >> ~4(bin) = 1011
# quindi
# sarà > 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
# 1011( = -5[x64] )


d = x ^ 5 #- -   1 - -  # confronto (con caret ' ^ '  1 su 1 = 0   e  tra  0  e  1   prevale 1)
# tra 4 (x = 0100)  e  5 ([bin] 0101)   sarà 1 ([0001])
# 0
# 1
# 0
# 0
# 0
# 1
# 0
# 1
# ---------
# 0
# 0
# 0
# 1 = 1[dec]

e = x >> 2 #- -   1 - -
f = x << 2 #- -   16
















































