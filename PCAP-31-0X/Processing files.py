###############################################################################


#############################################          PROCESSING  FILES


# dir utilizzata  >>>   C:\\PycharmProjects\\Py3\\...

# file default  >>>  C:\\PycharmProjects\\Py3\\filePCEP.txt


# 4.4.1.1 The os module   >>>   in fondo al file


###############################################################################


#     >>>>>>>    in lettura l'argument va espresso in bytes    <<<<<<<

#  per ogni operazione (read, readline, readlines...) bisogna aprire ([var] = open([dir+file], [mode]))
#  e chiudere - [var].close() una istanza "privata" per ogni operazione
#  non si può aprire (open()) un file, eseguire più operazioni e successivamente alla fine chiudere (close())


# ----  Nell'open() riveste fondamentale importanza il [mode] richiesto per il tipo di operazione
#
#  per intenderci non si può fare 'write'  di un file in open(mode : read) e viceversa  (I/O error)


print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  apertura stream  ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")

import sys

# stream = open('file', mode = 'r', encoding = None)
# stream.close()

#  'file'  :  path del file da aprire

#  mode = 'r'  tipo di apertura > r = read   (il file DEVE esistere)

#                                 w = write  (il file DEVE esistere)

#                                 a = append mode  (sovrascrittura, se il file non esiste viene creato al volo)

#                                 r+ = read & update  (il file DEVE esistere, both read and write operations are allowed)
#                                 w+ = write & update   (se il file non esiste viene creato al volo)
#                                                         both read and write operations are allowed
#
#                                 'b' alla fine della line = apertura in binary mode (può essere aggiunta alle mode sopra)
#                                                                                      rb, wb, ab, r+b, w+b)
#
#                                 't' alla fine della line = apertura in text mode (può essere aggiunta alle mode sopra)
#                                                                                    rt, wt, at, r+t, w+t))


# encoding  :  tipo di encoding (es. UTF-8)


print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  stream  ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")

# try:
#     stream = open("C:\\PycharmProjects\\Py3\\filePCEP.txt", "a")   # << << apertura
#     stream
#     #
#     # Processing goes here.
#     #
#     stream.close() # << << apertura
#     stream
#     è
#     sempre(buona
#     prassi) successivamente
#     "chiuso"
#     alla
#     fine
#     delle
#     ops
#     con
#     ' close() ' >> altrimenti
#     rimangono
#     troppi
#     stream
#     aperti
#
# except Exception as exc:  # gestione solita dell'exception
#     print("Cannot open the file:", exc)
#
# ###############################################################################
#
# >> >> TIPI
# DI
# STREAM << <<
#
# sono
# di
# 3
# tipi
# la
# declaration
# è
# nella
# lib[sys]
#
# al
# massimo
# import sys
#
# dall
# 'inizio e sei ok!
#
# #################################################################################
#
#
# -------------------------------------------------------------------------------------     sys.stdin
#
# stdin( as standard
# input)
#
# the
# stdin
# stream is normally
# associated
# with the keyboard, pre-open for reading and regarded as the
# primary
# data
# source
# for the running programs;
# the
# well - known
# input()
# function
# reads
# data
# from stdin by
#
# default.
#
# -------------------------------------------------------------------------------------     sys.stdout
#
# stdout( as standard
# output)
#
# the
# stdout
# stream is normally
# associated
# with the screen, pre-open for writing, regarded as the
# primary
# target
# for outputting data by the running program;
# the
# well - known
# print()
# function
# outputs
# the
# data
# to
# the
# stdout
# stream.
#
# -------------------------------------------------------------------------------------     sys.stderr
#
# stderr( as standard
# error
# output)
#
# the
# stderr
# stream is normally
# associated
# with the screen, pre-open for writing, regarded as the
# primary
# place
# where
# the
# running
# program
# should
# send
# information
# on
# the
# errors
# encountered
# during
# its
# work;
# we
# haven
# 't presented any method to send the data to this stream (we will do it soon, we promise)
# the
# separation
# of
# stdout(useful
# results
# produced
# by
# the
# program) from the stderr
#
# (error messages, undeniably useful but does not provide results)
# gives
# the
# possibility
# of
# redirecting
# these
# two
# types
# of
# information
# to
# the
# different
# targets.
#
# ################################################################################
#
# ########################################   selected constants useful for detecting stream errors:
#
#
# ########################################
#
#
# ---------------------------------------------------------------------      errno.EACCES → Permission
# denied
#
# The
# error
# occurs
# when
# you
# try, for example, to open a file with the read only attribute for writing.
#
# ---------------------------------------------------------------------      errno.EBADF → Bad
# file
# number
#
# The
# error
# occurs
# when
# you
# try, for example, to operate with an unopened stream.
#
# ---------------------------------------------------------------------      errno.EEXIST → File
# exists
#
# The
# error
# occurs
# when
# you
# try, for example, to rename a file with its previous name.
#
# ---------------------------------------------------------------------      errno.EFBIG → File
# too
# large
#
# The
# error
# occurs
# when
# you
# try to create a file that is larger than the maximum allowed by the operating system.
#
# ---------------------------------------------------------------------      errno.EISDIR → Is
# a
# directory
#
# The
# error
# occurs
# when
# you
# try to treat a directory name as the name of an ordinary file.
#
# ---------------------------------------------------------------------      errno.EMFILE → Too
# many
# open
# files
#
# The
# error
# occurs
# when
# you
# try to simultaneously open more streams than acceptable for your operating system.
#
# ---------------------------------------------------------------------      errno.ENOENT → No
# such
# file or directory
#
# The
# error
# occurs
# when
# you
# try to access a non-existent file / directory.
#
# ---------------------------------------------------------------------      errno.ENOSPC → No
# space
# left
# on
# device
#
# The
# error
# occurs
# when
# there is no
# free
# space
# on
# the
# media.




print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  stream  ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")




try:
    stream = open("C:\\PycharmProjects\\Py3\\filePCEP.txt", "a")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)




print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  diagnose stream  ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")




try:
    print("print esempio per impedire l'err")
    # Some stream operations.
except IOError as exc:
    print(exc.errno)  # <<<  .errno  sarebbe error number





print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  diagnose stream  ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")




from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  diagnose stream  ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")

import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")

    #  Actual processing goes here  ####

    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Key takeaways  exrc 3 ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print("\n▼￫￫￫￫￫  What is the expected output of the following code,\n assuming")

# that
# the
# file
# named
# file
# does
#
# not exist?  ￩￩￩￩￩￩￩￩▼\n")

import errno

try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")

#  -----output :  absent   >  IOError   error.errno == errno.ENOENT: no entry  file non esiste, quindi print("absent")


print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")

# Opening tzop.txt in read mode, returning it as a file object:
stream = open("C:\\PycharmProjects\\Py3\\filePCEP.txt", "rt", encoding="utf-8")

print('Lettura file :\n', stream.read())  # printing the content of the file
stream.close()

#  print(stream.close())  restituisce  None



print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")


from os import strerror

try:
    cnt = 0
    s = open('C:\\PycharmProjects\\Py3\\filePCEP.txt', "rt")
    ch = s.read(1)

    while ch != '':   #  >> > qui sono due apici singoli(' )  vicini

     print(ch, end='')  # end='' necessario!  (altrimenti print dei chars in colonna)
     cnt += 1
     ch = s.read(1)
     s.close()
     print("\n\n---(* tenendo presente anche [|spazio|]  ed  [|enter|] *) \nTot chars presenti nel file :", cnt)

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print("▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫     workdir   >>>        C:\\PycharmProjects\\Py3\\py1.txt   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩\n")

from os import strerror

try:
    cnt = 0
    s = open('C:\\PycharmProjects\\Py3\\py1.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as ex_io:
    print("I/O error occurred: ", strerror(ex_io.errno))

# strerr(ex_io.errno)

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print("▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫     workdir   >>>  readline()  C:\\PycharmProjects\\Py3\\py1.txt   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩\n")

# The method tries to read a complete line of text from the file
# and returns it as a string in the case of success. Otherwise, it returns an empty string.

#  con readline() legge l'intera riga e non i singoli chars

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('C:\\PycharmProjects\\Py3\\py11.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:",
          strerror(e.errno))  # nel caso ---output : I/O error occurred: No such file or directory

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print(
    "▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫     workdir   >>>  readlines()  C:\\PycharmProjects\\Py3\\filePCEP.txt   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩\n")

#  readelines() (senza arguments) prova a leggere TUTTE  le lines del file
# returns a list of strings, one element per file line.

s = open("C:\\PycharmProjects\\Py3\\filePCEP.txt")
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
s.close()

#  funzionamento di readlines()
# ---output:

# ['##################################\n']
# ['\n', '######          PROCESSING  FILES\n']
# ['\n', '##################################\n']
# ['\n', '\n', '         -----------------     file [filePCEP.txt]   -----------------\n']

#  trasforma tutto in una lista di elem string, compresi \n


print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print("▼￫￫￫￫￫￫￫￫￫  readlines()   workdir >>>  C:\\PycharmProjects\\Py3\\filePCEP.txt   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩\n")

s = open("C:\\PycharmProjects\\Py3\\filePCEP.txt")
print("\n---- readlines(20) : ")
print(s.readlines(20))
print("\n---- readlines(10) : ")
print(s.readlines(10))
print("\n---- readlines(5) : ")
print(s.readlines(5))
print("\n---- readlines(10) : ")
print(s.readlines(10))
print("\n**********    fine readlines  ")
s.close()

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print("▼￫￫￫￫￫￫￫￫￫  readlines()   workdir >>>  C:\\PycharmProjects\\Py3\\filePCEP.txt   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩\n")

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('C:\\PycharmProjects\\Py3\\filePCEP.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print("▼￫￫￫￫￫￫￫￫￫    workdir >>>  C:\\PycharmProjects\\Py3\\filePCEP.txt  REDUX ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩\n")

try:
    ccnt = lcnt = 0
    for line in open('C:\\PycharmProjects\\Py3\\filePCEP.txt',
                     'rt'):  # open() usato come obj del loop in read-text mode
        lcnt += 1  # (loop = iterable class)

        for ch in line:
            print(ch, end='')
            ccnt += 1

    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print("▼￫￫￫￫￫￫￫￫￫    workdir >>>  C:\\PycharmProjects\\Py3\\filePCEP.txt  |  write()    ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩\n")

#  writing a file opened in read mode won't succeed


from os import strerror

try:
    fo = open('C:\\PycharmProjects\\Py3\\PCEP_w1.txt', 'wt')  # A new file (newtext.txt) is created.
    for i in range(5):
        s = "line #" + str(i + 1) + "\n"
        for ch in s:
            fo.write(ch)
    fo.close()
    fo2 = open('C:\\PycharmProjects\\Py3\\PCEP_w1.txt', 'rt')
    print("Lettura file (read) :\n" + '\n' + "*" * 10 + '\n' + fo2.read() + '*' * 10)
    fo.close()
except IOError as e:
    print("I/O error : ", strerror(e.errno))

print('\n----apertura 2° istanza per read() --  Lettura fo2\n')

# apertura istanza open()
fo2 = open('C:\\PycharmProjects\\Py3\\py3test.txt', 'rt')

print("Lettura file (read) :\n" + fo2.read(), "\n******************* fine fo2.read\n")

fo2.close()  # chiusura istanza open()

# apertura istanza open()

print('\n----apertura 3° istanza per readlines(10) --  Lettura fo3 = open(...PCEP_w1.txt)')

fo3 = open('C:\\PycharmProjects\\Py3\\PCEP_w1.txt')

print('---   Echo fo3.readlines(10)  >> !!! ritorna una list !!!\n')

print('list : ', fo3.readlines(200))

fo3.close()  # chiusura istanza open()






print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###  Working with real files ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")
print("▼￫￫￫￫￫￫￫￫￫    workdir >>>  C:\\PycharmProjects\\Py3\\filePCEP.txt  |  write()    ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩\n")


from os import strerror
import sys

try:
    fo = open('C:\\PycharmProjects\\Py3\\wr1.txt', 'wt')
    for i in range(4):
        fo.write("line #" + str(i + 1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error : ", strerror(e.errno))

print("\nScrittura eseguita.\nLettura file wr1.txt in workdir C:\PycharmProjects\Py3\n")

try:
    r1 = open('C:\\PycharmProjects\\Py3\\wr1.txt', 'rt')
    print(r1.read())
    r1.close()
except IOError as io_err:
    sys.stderr.write("Error message")



#    ----    BYTE ARRAY  >>>  constructor fills the whole array with zeros.
###############################################


# specialized class Python uses to store amorphous data.

# Amorphous data is data which have no specific shape or form - they are just a series of bytes.


print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###     BYTE ARRAY  >>>    ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")

#  argument della func bytearray(x) è un integer compreso tra 0 e 255   sarebbro bytes

data = bytearray(10)  # (10) compreso tra 0 e 255

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b), end=' || ')  # ---output di valori esadecimali
    #  0xa || 0x9 || 0x8 || 0x7 || 0x6 || 0x5 || 0x4 || 0x3 || 0x2 || 0x1 ||

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###     BYTE ARRAY  write   ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('C:\\PycharmProjects\\Py3\\f_bin1.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
print("\n----Write bin")

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###     BYTE ARRAY  read   ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")

# (**)readinto : Read bytes into a pre-allocated, writable bytes-like object b, and return the number of bytes read.
#                       If the object is in non-blocking mode and no bytes are available, None is returned.

from os import strerror

data = bytearray(5)

try:
    bf = open('C:\\PycharmProjects\\Py3\\f_bin1.bin', 'rb')
    bf.readinto(data)  # (**)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###     BYTE ARRAY  read   ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼\n")

from os import strerror

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print("\n▼￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫  FILE PROCESSING   ----  ###     BYTE ARRAY  copying file   ###  ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩▼")
print("￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫    ###     C:\\PycharmProjects\\Py3\\py1.txt  >>>  py2.txt    ########\n")

#  Ricapitolo :
#  1. apertura flussi dei 2 (o più) files con associata gestione exception/s
#                                   vanno aperti in binario (mode 'rb' > source file --- 'wb' > destination file/s)
#  2. generazione spazio buffer di memoria con bytearray([#bytes])
#  3. op sui files
#  4. chiusura flussi con close()
#


from os import strerror

# srcname = input("Enter the source file name: ")
srcname = 'C:/PycharmProjects/Py3/py1.txt'
try:
    src = open(srcname, 'rb')  # apertura flusso indicato da srcname (in lettura 'rb')
    print('Source file acquisito\n')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

# dstname = input("Enter the destination file name: ")
dstname = 'C:/PycharmProjects/Py3/py2.txt'
try:
    dst = open(dstname, 'wb')  # apertura flusso indicato da srcname (in scrittura 'wb')
    print('File destinazione impostato (' + dstname[23:] + ') in ' + dstname[:23])
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)  # genera buffer con capienza 64k
total = 0

try:
    readin = src.readinto(buffer)  # riempie il buffer [buffer = bytearray(65536)] >> (lettura)
    print(f"Type di readin : {type(readin)}")  # <class 'int'>

    while readin > 0:
        written = dst.write(buffer[:readin])  # < slice [:readin] (va da 0 a valore di readin, riempie il necessario)
        total += written  # ￪￪￪￪ write tende a riempire tutto il buffer  ￪￪￪  (written type : <class 'int'> )
        readin = src.readinto(buffer)  # leggi contenuto buffer

except IOError as e:
    print("\nCannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

print('', total, 'byte(s) copiati con successo')
src.close()
dst.close()

src_file = open('C:\\PycharmProjects\\Py3\\py1.txt', 'rt')
dst_file = open('C:/PycharmProjects/Py3/py2.txt', 'rt')

print('Lettura src : \n' + src_file.read())
print('Lettura dest : \n' + dst_file.read())

src_file.close()
dst_file.close()






######################################################################


#######################    L A B


######################################################################


#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# 4.3
# .1
# .15
# LAB: Sorted
# character
# frequency
# histogram

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°




print("\n---------  OOP mod 4  --  4.3.1.15 LAB: Character frequency histogram --------")
print("------------     #####     dir utilizzata  >>>   C:/PycharmProjects/Py3/...")
print('\n   ----------------------------------------------------------------------   \n')

#   asks the user for the input file's name;
#   reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
#   prints a simple histogram in alphabetical order (only non-zero counts should be presented)

#  file path :  C:/PycharmProjects/Py3/mod4-lab1.txt

#  Create a test file for the code, and check if your histogram contains valid results

#   contenuto file C:/PycharmProjects/Py3/mod4-lab1.txt  >>>   aBc

#   -----output  :
#   a -> 1
#   b -> 1
#   c -> 1


#    RICORDA  :   per OGNI op sul file apri e chiudi un flusso

# print(f.read(1))         #  legge la quantità di bytes impostata (1)
#  che si traduce nell'output lettura 1° carattere
#  se piazzo read(2) legge 2 bytes  >>  quindi anche la seconda lettera e così via

import errno

src1_lab = input("Inserisci path del file (forma | C:/<dir1>/<dir2>/.../<file> | ) : ")

# input("Inserisci path del file (forma | C:/<dir1>/<dir2>/.../<file> | ) : ")
#  file path :  C:/PycharmProjects/Py3/mod4-lab1.txt


# strm1 = open('C:/PycharmProjects/Py3/mod4-lab1.txt', 'rt')  #  questa apertura va inserita nel try
#  se c'è bisogno di gestire exception


try:
    strm1 = open(src1_lab, 'rt')
    read1 = strm1.read()
    print('\nFile presente, check se vuoto...\n')
    strm1.close()

except IOError as io_err:
    if io_err.errno == errno.ENOENT:
        strm1.close()
        print('Il file non esiste')

ch = ' '
lst_strm = []
dct_strm = {}

strm1 = open(src1_lab, 'rt')

while ch != '':
    ch = strm1.read(1)

    if ch != '':
        lst_strm.append(ch.lower())

if not lst_strm:
    strm1.close()
    print("File vuoto...")
    exit(0)
else:
    with open(src1_lab, "rt") as rd1:
        print("\nCheck -> OK!\n\n---- Lettura contenuto txt designato :\n", rd1.read(), "\n", "--" * 10,
              end='   fine txt\n')

strm1.close()

for k in lst_strm:
    c1 = lst_strm.count(k)
    dct_strm.update({f"{k}": f"{c1}"})

print('\n----------------Output finale richiesto dal lab :\n')
for elem in dct_strm.keys():
    val = dct_strm.__getitem__(elem)
    print(elem, end=f" -> {val}\n")






print("\n---------  OOP mod 4  --   4.3.1.16 LAB: Sorted character frequency histogram   --------")
print("------------     #####     dir utilizzata  >>>   C:/PycharmProjects/Py3/...    #####      ")
print('\n   ----------------------------------------------------------------------   \n')





# Your task is to make some amendments, which generate the following results:
#
#     the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)

#     the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist'
#     (it should be concatenated to the original name)
#

#  file path :  'C:/PycharmProjects/Py3/mod4-lab2.txt'

#  Note: You cannot sort a list that contains BOTH string values AND numeric values.


try:
    strm1 = open('C:/PycharmProjects/Py3/mod4-lab1.txt', 'rt')
    read1 = strm1.read()
    print('\n---- File presente, echo di conferma :\n\n', read1, '\n\n ----------  fine file txt')
    strm1.close()

except IOError as io_err:
    if io_err.errno == errno.ENOENT: print('Il file non esiste')

print('\ncontinuo...\n')

strm1 = open('C:/PycharmProjects/Py3/mod4-lab1.txt', 'rt')

ch = ' '
lst_strm = []
dct_strm = {}

while ch != '':
    ch = strm1.read(1)

    if ch != '':
        lst_strm.append(ch.lower())
        print("lista lettura : ", lst_strm)

for k in lst_strm:
    print(k, end='')
    c1 = lst_strm.count(k)
    dct_strm.update({f"{k}": f"{c1}"})
    print(c1, end=' - ')

print('\n----------  \nDict finale : ', dct_strm)

print('\n----------------Output finale richiesto dal lab :\n')
for elem in dct_strm.keys():
    val = dct_strm.__getitem__(elem)
    print(elem, end=f" -> {val}\n")

import errno

src1_lab2 = 'C:/PycharmProjects/Py3/mod4-lab2.txt'
# input("Inserisci path del file (forma | C:/<dir1>/<dir2>/.../<file> | ) : ")

try:
    strm1 = open(src1_lab2, 'rt')
    read1 = strm1.read()
    print('\nFile presente, check se vuoto...\n')
    strm1.close()

except IOError as io_err:
    if io_err.errno == errno.ENOENT:
        strm1.close()
        print('Il file non esiste')

ch = ' '
lst_strm = []
dct_strm = {}

strm1 = open(src1_lab2, 'rt')

while ch != '':
    ch = strm1.read(1)

    if ch != '':
        lst_strm.append(ch.lower())

if not lst_strm:
    strm1.close()
    print("File vuoto...")
    exit(0)
else:
    with open(src1_lab2, "rt") as rd1:
        print("\nCheck -> OK!\n\n---- Lettura contenuto txt designato :\n", rd1.read(), "\n", "--" * 10,
              end='   fine txt\n')

strm1.close()

for k in lst_strm:  # crea dict con i value = ricorrenze
    c1 = lst_strm.count(k)
    dct_strm.update({f"{k}": f"{c1}"})
    g_dict = dct_strm.update({f"{k}": f"{c1}"})

list_tup1 = list(dct_strm.items())

list_val = list(sorted(dct_strm.values(), reverse=True))

dct_strm2 = {}

for p1 in list_val:  # ['4', '3', '2']
    xtup1 = 0
    for p2 in list_tup1:  # [('c', '4'), ('b', '2'), ('a', '3')]
        if p1 == list_tup1[xtup1][1]:
            dct_strm2.update({f"{list_tup1[xtup1][0]}": f"{p1}"})
        else:
            xtup1 += 1
            continue

print("\nDictionary ordinato per value maggiore : ", dct_strm2)

print("\n---------------------  output ++ scrittura su file :\n")

src2_lab2 = 'C:/PycharmProjects/Py3/mod4-lab2_hist.txt'

with open(src2_lab2, 'w') as lab2:
    for key in dct_strm2.keys():
        value = dct_strm2.__getitem__(key)
        lab2.write(f"{key} --> {value}\n")
        print(f"{key} --> {value}")

lab2.close()

print("\nEseguita scrittura dell'output su file mod4-lab2_hist.txt")
print("Check se lettura OK...\n")

lab2 = open(src2_lab2, 'rt')

print('Lettura file : ')
print('------------')
print(lab2.read(), '\n------------   fine txt')

lab2.close()




print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫   T E S T  ###   4.3.1.17LAB: Evaluating students results  --￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩  ↺▼")

txt = 'C:/PycharmProjects/Py3/Jekyll.txt'


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    print("Bad line found....")


class FileEmpty(StudentsDataException):
    pass
    # Write your code here.


from os import strerror

flux1 = open(txt, 'rt')
r1 = flux1.readlines()

dct_pers = {}
dct_voti = {}
dct_nomi = {}

try:
    lst_let = []

    for x in r1:  # qua prende gli elems (str) della lista
        if x == '': raise BadLine
        lst_let.append(x)

    print(f"\nLista stringhe : {lst_let}\n")
    dct_pers.update()

except IOError as exc:
    flux1.close()
    print("I/O error : ", strerror(exc.errno))

flux1.close()
cnt = 0

lst_nomi = []
# lst_cogn = []

for string1 in lst_let:
    for y in string1:
        if not y.isalpha():
            continue
        elif y.isupper():
            cnt += 1
            if cnt > 1:
                cnt = 0
                print(end=' ')
        lst_nomi.append(y)
        print(y, end='')
    print()

# print(f"\nDictionary persone : {dct_pers}")
# print(f"\nLista nomi finale : {lst_nomi}\n")
#
# print('\n-------------------------------------------------------------------------------')
# print('---------------------------------------------------------------------------------')
# print('---------------------------------------------------------------------------------\n')

val2 = 0
nc1 = ''
nc2 = ''
cnt_l1 = 0
dct_nomi2 = {}

for k1 in lst_nomi:
    nc1 = nc1 + k1

    if k1.isupper():
        if cnt_l1 == 3:
            cnt_l1 = 1
            nc1 = k1
            val2 += 1

        elif cnt_l1 == 1:
            cnt_l1 += 1

        else:
            cnt_l1 += 1

    if k1.islower():
        if cnt_l1 == 0:
            nc2 = nc1
            dct_nomi2.update({f"line{val2}": f"{nc2}"})

        if cnt_l1 == 2:
            nc2 = nc1
            cnt_l1 += 1
            dct_nomi2.update({f"line{val2}": f"{nc2}"})

        nc2 = nc1
        dct_nomi2.update({f"line{val2}": f"{nc2}"})

print()

# print('-- -- -- -- Dictionary completo : ', dct_nomi2)

#  {'0': 'JohnSmith', '1': 'AnnaBoleyn', '2': 'JohnSmith', '3': 'AnnaBoleyn', '4': 'AndrewCox'}

# print('\n-----------------------------------------\n')

lst_n2 = []

for nome in lst_nomi:
    nome.join(nome)
    if nome.isupper():
        cnt += 1
        nome.join(nome)
        if cnt == 2:
            nome.join(nome)
            print(' ', end='')
            cnt = 1
    print(f"{nome}", end='')

flux1 = open(txt, 'rt')

# print(f"\n---------------dict nomi : {dct_nomi}\n")

try:
    lst_voti = []
    lst2_temp = []

    for x in r1:  # qua prende gli elems (stringhe) della lista
        for ch1 in flux1.readline():  # qua scompone la string char by char
            if ch1 == '': raise Exception
            if not chr(46) <= ch1 <= chr(57):
                continue
            else:
                # print(ch1, end='')
                lst_voti.append(ch1)

except IOError as exc:
    flux1.close()
    print("I/O error : ", strerror(exc.errno))

print()

# print('\n\n-----  voti float -----Lista voti : ', lst_voti, '\n')

lst_dec = []
lst_int = []
lst_f = []
dct_v1 = {}

ped1 = 0
key = 1
dct_int1 = {}

for k1 in lst_voti:  # ['5', '4', '.', '5', '2', '1', '1', '1', '.', '5']
    if not k1 == '.' and ped1 <= len(lst_voti):
        k1_int = int(k1)
        lst_int.append(k1_int)
        lst_f.append(k1_int)
        dct_v1.update({f"line{key}": f"{k1_int}"})
        ped1 += 1
    else:
        if ped1 == len(lst_voti): continue
        key = ped1
        k1_float = float(lst_voti[ped1 - 1] + k1 + lst_voti[ped1 + 1])
        lst_dec.append(k1_float)
        lst_f.append(k1_float)
        dct_v1.update({f"line{key}": f"{k1_float}"})
        del lst_int[-1]
        del lst_voti[ped1 + 1]
        del lst_f[-2:-1]
        ped1 += 1

# print('\n----   lista solo voti float : ', lst_dec)  #   [4.5, 1.5]
#
# print('\n--------   lista voti interi  : ', lst_int)   #    [5, 2, 1, 1]
#
# print('\n--------   lista voti tot ordinata  : ', lst_f)   #    [5, 4.5, 2, 1, 1, 1.5]
#
# print('\n--------   DICTIONARY tot ordinata  : ', dct_v1)
#
# print('\n--------   DICTIONARY tot interi  : ', dct_int1)

# for


#
# print('\n------  TEMP  ----------  TEMP  -------  dct_n1 : ')
# print('------  TEMP  ----------  TEMP  -------  dct_n1 : \n')


dct_num1 = {}
dct_num2 = {}
l_cnt = 0
lst_intg = []
numb1 = 0
line1 = ''
n_cnt = 0
num_prev = 0

for line1 in r1:
    l_cnt += 1
    for numb1 in line1:
        if numb1 == '.':
            dct_num2.popitem()
            dct_num1.popitem()
            n_cnt = 0
            break
        elif chr(48) <= numb1 <= chr(57):
            dct_num2.update({f"line{l_cnt}": f"{numb1}"})
            dct_num1.update({f"{numb1}": f"line{l_cnt}"})
            if n_cnt >= 2:
                dct_num2.update({f"line{l_cnt}": f"{lst_intg[-1] + numb1}"})
                dct_num1.update({f"{numb1}": f"line{l_cnt}"})

# print('\n-----1 1 1 1 1---------  Dict post deleting:  ', dct_num1)  # {'5': 'line1', '2': 'line3', '8': 'line4', '7': 'line4'}
#
# print('\n----2 2 2 2 2----------  Dict post deleting (lines SENZA virgola):  ', dct_num2) # {'line1': '5', 'line3': '2', 'line4': '7'}
#
# #print('\n--------------  List post deleting:  ', lst_intg)

dct_num3 = {}

# for key1,value1 in dct_num1.items():
#     for key2, value2 in dct_num2.items():
#         if value1 == key2 :
#             while True:
#                 dct_num3.update({f"{value1}": f"{key1+value2}"})
#                 print('\n--------------  Dict WHILE:  ', dct_num3)
#                 break
#             break

cnt_w = 0

for key2, value2 in dct_num2.items():
    while True:
        for key1, value1 in dct_num1.items():
            if key2 == value1:
                cnt_w += 1
                if cnt_w >= 3:
                    dct_num3.update({f"{key2}": f"{key1 + value2}"})
                    break
        break

# print('\n--------   lista voti interi  : ', lst_int)   #    [5, 2, 1, 1]
# print('\n-----3 3 3 3 3 3 3 ---------  Dict FINAL DIAHNE:  ', dct_num3)
#
# print('\n---------------------3 3 3 3 3 3 3 ----------------------------------\n')

flux2 = open(txt, 'rt')
rls1 = flux2.readlines()

cnt_chr = 0
cnt_num = 0
cnt_lns = 0

for line in rls1:
    cnt_lns += 1
    for chr in line:
        if chr.isalpha():
            continue
        elif chr.isdigit() or chr == '.':
            cnt_num += 1
            print(chr, end='')

    else:
        fl1 = flux2.read(cnt_chr)
        fchr = flux2.read(cnt_num)
        # print('\n----------------Echo valore flux2.read(cnt_chr) >> else : ', fl1)
        # #print('\n----------------Echo valore flux2.read(cnt_num) >> else : ', fchr)

# print('\nNumero lines = ', cnt_lns)
#
#
# print('\n----   lista solo voti float : ', lst_dec)  #   [4.5, 1.5]
#
# print('\n--------   lista voti interi  : ', lst_int)   #    [5, 2, 1, 1]
#
# print('\n--------   lista voti tot ordinata  : ', lst_f)   #    [5, 4.5, 2, 1, 1, 1.5]
#
# print('\n--------   DICTIONARY tot ordinata  : ', dct_v1)
#
# print('\n--------   DICTIONARY tot interi  : ', dct_int1)
#
# print('\n-----1 1 1 1 1---------  Dict post deleting:  ', dct_num1)  # {'5': 'line1', '2': 'line3', '8': 'line4', '7': 'line4'}
#
# print('\n----2 2 2 2 2----------  Dict post deleting (lines SENZA virgola):  ', dct_num2)

copy1dct = dct_num2.copy()

print()

flux = open(txt, 'rt')
# flux_t = open(txt, 'rt')
dct_str = {}

rls1 = flux.readlines()

cnt_chr = 0
cnt_num = 0
kc1 = 0
lst_9 = []

for line9 in rls1:
    kc1 += 1
    cnt_num = 0
    for chr in line9:
        if chr.isalpha(): continue
        if chr == '.':
            cnt_num = 0
            del lst_9[:]
            dct_num2.__delitem__(f"line{kc1 - 1}")
            continue
        if chr.isdigit():
            cnt_num += 1
            lst_9.append(chr)
            if cnt_num > 1:
                chr_pre = lst_9[-2:-1]
                for elem1 in chr_pre:
                    chr = elem1 + chr
                    chr = int(chr)
                dct_num2.update({f"line{kc1 - 1}": f"{chr}"})

# print('\n\nQ.tà char = ', cnt_chr)
# print('\nQ.tà numeri = ', cnt_num)

# print('\n----2 copia copia cpia 2 2----------  Dict_num2 COPIA:  ', copy1dct)
# print('\n Dct num update finale : ', dct_num2)

print()

ele_num = -1
dct_pntg = {}

for ele_f in lst_f:
    ele_num += 1
    dct_pntg.update({f"line{ele_num}": f"{ele_f}"})

# print('\n----------------Dct dct_pntg update con INTERI : ', dct_pntg)


for key1, val1 in dct_num2.items():
    for key2, val2 in dct_pntg.items():
        if key1 == key2:
            dct_pntg.update({f"{key2}": f"{val1}"})
        else:
            continue

# print('\n !!!!!  dct_num2 dopo eliminazione keys superflue : ', dct_num2)
#
# print('\n----2 copia copia cpia 2 2----------  Dict_num2 COPIA:  ', copy1dct)
# print('\n Dct dct_pntg update dct_pntg  dct_pntg : ', dct_pntg)
# print('\n--------   lista voti tot ordinata  : ', lst_f)   #    [5, 4.5, 2, 1, 1, 1.5]
#
#
#
# print('\n-------------*** *** *** dctnry1 = {} update---------\n')


cntr = -1

for key1, value1 in copy1dct.items():
    for key2, value2 in dct_pntg.items():
        if key1 != key2:
            continue
        elif value1 != value2:
            continue
        else:
            key2_index = key2
            dct_pntg.pop(key2)
            break

# print('\n Dct FINAL dct_pntg : ', dct_pntg)
# #print('\n DCT FINAL dctnry1.update -- COPIA  --  COPIA !!! : ', dctnry1)
#
# print('\n-----------------       FINAL dctnry1         -----------------------------------\n')

dctnry1 = {}
cntr = 0

for key, value in dct_pntg.items():
    dctnry1.update({f"line{cntr}": f"{value}"})
    cntr += 1

# print('\n DCT FINAL dctnry1.update  : ', dctnry1)
# print('\n DCT FINAL dct_nomi2  : ', dct_nomi2)


dct_pp1 = {}
ctr_len = 0
lst_seq1_full = []
lst_seq1_nomi = []
lst_seq1_pntg = []

for key1, value1 in dct_nomi2.items():
    for key2, value2 in dctnry1.items():
        if key1 == key2:
            ctr_len += 1
            lst_seq1_nomi.append(value1)
            lst_seq1_full.append(value1)
            val2_float = float(value2)
            lst_seq1_pntg.append(val2_float)
            lst_seq1_full.append(val2_float)
            dct_pp1.update({f"{value1}": f"{val2_float}"})
            break

dct_pp1_sorted_lst = sorted(dct_pp1)
# print('\n****   ****  ***  DICTIONARY COMPLETO   ::::  ', dct_pp1)
# print('\n****   ****  ***  LISTA NOMI (in ord alfbet) dct_pp1_sorted_lst>>>  ', dct_pp1_sorted_lst)
# print('\n****   ****  ***  LISTA SEQ1 ordinata (nomi) lst_seq1_nomi>>>  ', lst_seq1_nomi)
# print('\n****   ****  ***  LISTA SEQ1 ordinata (punteggio) lst_seq1_pntg>>>  ', lst_seq1_pntg)
# print('\n****   ****  ***  LISTA SEQ1 ordinata (nomi >> punteggio) lst_seq1_full>>>  ', lst_seq1_full)


print('\n-----------------       FINAL         -----------------------------------\n')

dct_rep = {}
sum1_float = 0.0

i = 0
for nm1 in dct_pp1_sorted_lst:
    dct_rep.update({f"{nm1}": f"{float(i)}"})

# print('\n****   ****  ***  DICTIONARY COMPLETO   dct_rep::::  ', dct_rep)
# print('\n****   ****  ***  LISTA SEQ1 ordinata (nomi) lst_seq1_nomi>>>  ', d)
print()

# ped1 = 0
# ped2 = 0
# lst_sum1 = []
# sum1 = 0
dct_z = {}

for key1, value1 in dctnry1.items():
    for key2, value2 in dct_nomi2.items():
        if key1 == key2:
            dct_z.update({f"{value1}": f"{value2}"})

# print("\n\nDCT z finale : ", dct_z)
#
# print("\n-------------------------------------------------------------\n")

k2 = 0.0
k3 = 0.0
dct_ff2 = {}
i = 0

for elem1 in dct_pp1_sorted_lst:
    for key, val in dct_z.items():
        if elem1 == val:
            k1_f = float(key)
            x1 = dct_z.setdefault(key, k3)
            k3 = k2 + k1_f
            dct_ff2.update({f"{x1}": f"{k3}"})
            k2 = k1_f

for key1, value1 in dct_ff2.items():
    print(f"\nCandidato : {key1} - Punteggio (somma) = {value1}")

flux.close()
flux1.close()
flux2.close()

###########################################################################


#      4.4.1.1 The os module


###########################################################################


# 'C:/PycharmProjects/Py3/...'

import platform

print(platform.uname())

#  uname_result(system='Windows', node='Vinz7-G77Titan',
#  release='11', version='10.0.26100', machine='AMD64')


print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The os module   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼")

import os, stat  # stat serve ad assegnare la 'mode' alla creazione della dir

print(os.name)  # nt

os.mkdir('C:/PycharmProjects/Py3/dir esempio (os_mkdir)/')
#  senza il link ('C:/PycharmProjects/Py3/)
#  crea nella cartella dove si trova i files qui
#  a fianco nel tree Project
#  >>>  es.    os.mkdir("my_first_directory")
#  crea una cartella ("my_first_directory") in <Essentials 2 - MODULO 4>


print(os.listdir())  # SENZA argument
# ----output :   >>  ritorna una list elenco dei files della current dir
#  CON argument (path)  >>  ritorna una list elenco dei files della vdir preselezionata

# ['Jekyll code.py', 'MOD 4  --  L A B 1.py',
# 'MOD 4  --  L A B 2.py', 'MOD 4 - Generators & Closures.py',
# 'MOD 4 - OS module.py', 'MOD 4 - Processing files II.py', 'MOD 4 - Processing files.py',
# 'my_first_directory', 'TEST 3.py', 'TEST 4.py']


#  tip ____  eseguendo una seconda volta raise a FileExistsError  <<<<<
#  ---output :

# FileExistsError: [WinError 183] Impossibile creare un file,
# se il file esiste già: 'C:/PycharmProjects/Py3/dir esempio (os_mkdir)/'


print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The os module   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼")

# Import os and stat Library
import os, stat

# Change the mode of path
os.chmod('C:/PycharmProjects/Py3/dir esempio (os_mkdir)/', stat.S_IWRITE)  # Write by owner

#  -------------------------------------------    tipi di modes per os.chmod
# stat.S_ISUID - Set user ID on execution
# stat.S_ISGID - Set group ID on execution
# stat.S_ENFMT - Record locking enforced
# stat.S_ISVTX - Save text image after execution
# stat.S_IREAD - Read by owner
# stat.S_IWRITE - Write by owner
# stat.S_IEXEC - Execute by owner
# stat.S_IRWXU - Read, write, and execute by owner
# stat.S_IRUSR - Read by owner
# stat.S_IWUSR - Write by owner
# stat.S_IXUSR - Execute by owner
# stat.S_IRWXG - Read, write, and execute by group
# stat.S_IRGRP - Read by group
# stat.S_IWGRP - Write by group
# stat.S_IXGRP - Execute by group
# stat.S_IRWXO - Read, write, and execute by others
# stat.S_IROTH - Read by others
# stat.S_IWOTH - Write by others
# stat.S_IXOTH - Execute by others


print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The os module ## makedirs ￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

import os

os.makedirs("C:/PycharmProjects/Py3/my_first_directory/my_second_directory")
# crea la sottodir my_second_directory dopo aver creato la prima dir  my_first_directory


os.chdir("C:/PycharmProjects/Py3/my_first_directory/")  # e ritorna nella path my_first_directory/
print(os.listdir())  # list del contenuto
#   ---- output :  ['my_second_directory']


print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The os module   ## os.getcwd()    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

import os

os.makedirs("my_first_directory/my_second_directory")
# crea il path "my_first_directory/my_second_directory"


os.chdir("my_first_directory")  # imposta gestione della dir "my_first_directory"
print(os.getcwd())

os.chdir("my_second_directory")  # imposta gestione della dir "my_second_directory"
print(os.getcwd())

#  (tenendo presente line 103 -> os.chdir("C:/PycharmProjects/Py3/my_first_directory/"))
#       la current dir è C:/PycharmProjects/Py3/my_first_directory/


#  ---- output :

# C:\PycharmProjects\Py3\my_first_directory\my_first_directory
# C:\PycharmProjects\Py3\my_first_directory\my_first_directory\my_second_directory


print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The os module   ## os.rmdir()    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

import os

os.mkdir("my_first_directory")  # crea la dir
print(os.listdir())  # lista la dir

os.rmdir("my_first_directory")  # rimuove la dir
print(os.listdir())  # lista la 'rimozione'

#  >>>>>     removedirs()   >>>  rimuove più dirs
#   piazzando tutti i path precisi


print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The os module   ## os.system()    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

#  ritorna un cmd impostato come string

import os

returned_value = os.system("mkdir my_first_directory")  # os.system + cmd str(mkdir my_first_directory)
print(returned_value)

################################################################################################


###    MODULO 4  --  lab e section summary

# os
# module

################################################################################################


print("\n---------       OOP mod 4  --  4.4.1.8 LAB: The os module        --------\n")

#  "C:/PycharmProjects/Py3/"

from os import chdir, listdir


def pthfindir(path, dir):
    chdir(f"C:/PycharmProjects/Py3/{path}")
    lst1 = listdir(f"C:/PycharmProjects/Py3/{path}")

    while dir in lst1:
        for cdir1 in lst1:
            if cdir1 == dir:
                chdir(f"C:/PycharmProjects/Py3/{path}/{cdir1}")  # entra nella dir
                print('\n---Liv 1----  Echo getcwd() sub-zero >> ', getcwd()[22:])
                # chdir(f"C:/PycharmProjects/Py3/{path}/")
                # yield getcwd()[22:]

            chdir(f"C:/PycharmProjects/Py3/{path}/{cdir1}")
            lst1 = listdir(f"C:/PycharmProjects/Py3/{path}/{cdir1}")
            for sub in lst1:
                if sub == dir:
                    chdir(f"C:/PycharmProjects/Py3/{path}/{cdir1}/{sub}")
                    print('\n--Liv 2-----  Echo getcwd() sub1 >> ', getcwd())
                    # yield getcwd()[22:]
                    # lst2 = listdir(f"C:/PycharmProjects/Py3/{path}/{cdir1}/{sub}")
                else:
                    lst2 = listdir(f"C:/PycharmProjects/Py3/{path}/{cdir1}/{sub}")
                    for sub2 in lst2:
                        if sub2 == dir:
                            chdir(f"C:/PycharmProjects/Py3/{path}/{cdir1}/{sub}/{sub2}")
                            print('\n---Liv 3----  Echo getcwd() sub2 >> ', getcwd()[22:])
                            # yield getcwd()[22:]
    # yield getcwd()


# for x1 in pthfindir("./tree", 'python'): print(x1)
pthfindir("./tree", 'python')

print("\n---------       OOP mod 4  --  4.4.1.9   SECTION SUMMARY        --------\n")

import os

os.mkdir("hello")
print(os.listdir())  # ['hello']








































































