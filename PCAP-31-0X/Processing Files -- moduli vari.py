################################################################################################



###    MODULO 4  --  parte finale   >>>>   Moduli vari



## datetime

##   line 409  >>  CALENDAR
################################################################################################




print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The datetime module   ## datetime    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")



from datetime import date

my_date = date(2019, 11, 4)
print(my_date)   #  output :  2019-11-04





print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The datetime module   ## datetime    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")


from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print("------------------- EURO format\n")
print(f"Data EU : {today.day}/{today.month}/{today.year}")

#   ----- output :
# Today: 2025-06-25
# Year: 2025
# Month: 6
# Day: 25




print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The datetime module   ## datetime    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")



from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp) # Timestamp: 1750873366.9088955
                               # il float in questione rivela i secondi passati dal 1 gen 1970
                               # alla data del momento

d = date.fromtimestamp(timestamp)
print("Date:", d)    #    Date: 2025-06-25




print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫     Mod IV  The datetime module   ## fromisoformat    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

#  imposta data custom in ord (AAAA, MM, GG)

#  se impostata diversamnete >> date.fromisoformat('26-11-2032')
                # ValueError: Invalid isoformat string: '26-11-2032'


from datetime import date

d = date.fromisoformat('2019-11-04')
print(d)

# print('Data sec : ', date.fromisoformat('26-11-2032'))
# ValueError: Invalid isoformat string: '26-11-2032'




print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ## replace(year, month, day) ￩￩￩￩￩￩￩￩ ↺▼\n")

#  semplice replace()

from datetime import date

d = date(1991, 2, 5)
print(d)  #  1991-02-05

d = d.replace(year=1992, month=1, day=16)
print(d)   #  1992-01-16




print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ## weekday() ￩￩￩￩￩￩￩￩ ↺▼\n")
# segue la ISO 85601 specification.

from datetime import date

d = date(2025, 6, 25)
print(d.weekday())

# ritorna il giorno della week as integer (0 = lun  -->  6 = domenica  )
# OGGI è mercoledì  >>>  output : 2

print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ## isoweekday() ￩￩￩￩￩￩￩￩ ↺▼\n")

from datetime import date

d = date(2025, 6, 25)
print(d.isoweekday()) # segue la ISO 85601 specification.

# ritorna il giorno della week as integer (1 = lun  -->  7 = domenica  )
# OGGI è mercoledì  >>>  output : 3




print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ## time(hour....) ￩￩￩￩￩￩￩￩ ↺▼\n")



# time(hour, minute, second, microsecond, tzinfo, fold)
#                                           ￪       ￪
#                                     timezone   amount of time that a program or process
#                                                takes to run from start to finish as measured
#                                                by a person (aka real-world time, clock time,
#                                                wall-clock time
#                                                or -- more accurately -- elapsed real time)



from datetime import time

t = time(14, 53, 20, 1)  # (h, mins, sec, fold=1)

print("Time:", t)   #  Time: 14:53:20.000001
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

###  resto output :   (come da impostazione)
# Hour: 14
# Minute: 53
# Second: 20
# Microsecond: 1

print(f"\nora esatta : {time.hour}:{time.minute}")


print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ## .time (sleep)￩￩￩￩￩￩￩￩ ↺▼\n")


import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(1)




print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ## .ctime ￩￩￩￩￩￩￩￩ ↺▼\n")



import time

timestamp = 1472469386  # deconversione Unix epoch da totale millisec a data e ora precisi
print(time.ctime(timestamp))

#  ---- output : Wed Aug 31 20:46:20 2016  (= 1472669180)

#  ---- output : 1472469386 -> Mon Aug 29 13:16:26 2016



print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module  gmtime() - localtime() funcs  ￩￩￩ ↺▼")
print("▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ++ time.struct_time class   ￩￩￩￩￩￩￩￩ ↺▼\n")


# class specializzata in objects puntuali tenedo presente il timestamp
# in millisec totali (dal 1/1/1970, Unix epoch), segue lista objects :

# time.struct_time:

#     OBJECT    #    description

#     tm_year   # specifies the year
#     tm_mon    # specifies the month (value from 1 to 12)
#     tm_mday   # specifies the day of the month (value from 1 to 31)
#     tm_hour   # specifies the hour (value from 0 to 23)
#     tm_min    # specifies the minute (value from 0 to 59)
#     tm_sec    # specifies the second (value from 0 to 61 )
#     tm_wday   # specifies the weekday (value from 0 to 6)
#     tm_yday   # specifies the year day (value from 1 to 366)
#     tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
#     tm_zone   # specifies the timezone name (value in an abbreviated form)
#     tm_gmtoff # specifies the offset east of UTC (value in seconds)




import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

#####     ---- output time.gmtime(timestamp)  >>>  struct_time object

# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0,
# tm_wday=0, tm_yday=308, tm_isdst=0)


#####  ---- output time.localtime(timestamp)   >>>  ritorna local time

# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=15, tm_min=53, tm_sec=0,
# tm_wday=0, tm_yday=308, tm_isdst=0)



print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module  asctime() e mktime() funcs  ￩￩￩ ↺▼")
print("▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ++ time.struct_time class   ￩￩￩￩￩￩￩￩ ↺▼\n")



import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))  #  coverte obj struct_time (o una tupla) in string
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))  # converte obj struct_time in msec Unix epoch

# tip : se non piazzi l'argument a .asctime() ritorna autom
# il risultato local time


#   ----- output :

# Mon Nov  4 14:53:00 2019
# 1572875580.0



print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ++ datetime objcts   ￩￩￩￩￩￩￩￩ ↺▼\n")

# datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)
# TUTTI i param passati sono read-only



from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)  #  Datetime: 2019-11-04 14:53:00
print("Date:", dt.date())  # (passa solo la data) Date: 2019-11-04
print("Time:", dt.time())  # (passa solo l'orario) Time: 14:53:00





print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime module   ++ datetime methods   ￩￩￩￩￩￩￩￩ ↺▼\n")



from datetime import datetime, timezone

print("today:", datetime.today())
print("now:", datetime.now())
#print("utcnow:", datetime.utcnow()) #  <<<<  DEPRECATION WARNING *

# * DEPRECATION WARNING :
# datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version.
# Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

print('\n(.utcnow deprecation) -- >>>  importing timezone from datetime')
print('Utilizzo datetime.now(timezone.utc)', datetime.now(timezone.utc))

#  (comunque) -------  output :

# today: 2025-06-26 17:08:14.948544
# now: 2025-06-26 17:08:14.948556
# utcnow: 2025-06-26 15:08:14.963977   #  time-zone
# datetime.now(timezone.utc) 2025-06-26 15:20:22.247471+00:00

# ritornano tutti la stessa data/orario con l'unica differenza del ritardo output





print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime time formatting   ++ .strftime   ￩￩￩￩￩￩￩￩ ↺▼\n")


# utilizzo di varie directives : %Y , %m , %d , %a (abbrev. weekday) , %A (weekday full)....

from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))




print("\n▼↻  ￫￫￫￫￫  Mod IV  The datetime time formatting   ++ .strftime   ￩￩￩￩￩￩￩￩ ↺▼\n")



from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

print(dt.strftime("%Y/%B/%d %H:%M:%S"))
print(dt.strftime("%d/%B/%Y %H:%M:%S"))





import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))



#  to be continued....




######################################################################         DATETIME LAB




print("\n--------   MODULO 4  --  4.5.1.22 LAB: The datetime and time modules --------\n")



from datetime import date, datetime, time

dt = datetime(2020, 11, 4, 14, 53, 00)
d = date(2020, 11, 4)
t1 = time(14, 53, 00)


print(dt.strftime('%Y/%m/%d -- %H:%M:%S'))  #  2020/11/04 -- 14:53:00


print(d.strftime('%y/%B/%d --'), end='')
print(t1.strftime(' %H:%M:%S %p '))   #  20/November/04 --  14:53:00 PM


print(d.strftime('%a, %Y %b %d'))  #  Wed, 2020 Nov 04

print(d.strftime('%A, %Y %B %d'))  #   Wednesday, 2020 November 04

print(d.strftime('Weekday: %w'))   #  Weekday: 3

print(d.strftime('Day of the year: %j'))   #  Day of the year: 309

print(d.strftime('Week number of the year: %U'))   #   Week number of the year: 44






print("\n--------   MODULO 4  --  4.5.1.23 SECTION SUMMARY  datetime --------\n")



from datetime import datetime

dt1 = datetime(2020, 9, 29, 14, 41, 0)
dt2 = datetime(2020, 9, 28, 14, 41, 0)

print(dt1 - dt2)    #   1 day, 0:00:00






#-----------------------------------------------------------------------------------------------------------------------

#                                                CALENDAR  module

#-----------------------------------------------------------------------------------------------------------------------


print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV   --  CALENDAR  module --   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

# #   optional
#
#     w – date column width (default 2)
#     l – number of lines per week (default 1)
#     c – number of spaces between month columns (default 6)
#     m – number of columns (default 3)



import calendar
print(calendar.calendar(2025, m=4))   #  4 mesi per riga


calendar.prcal(2025, m=5)   #  5 mesi per riga

#   -------  stesso output  :  calendario




print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV   --  CALENDAR  .month()   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")




import calendar
print(calendar.month(2025, 6))

calendar.prmonth(2025, 6)


#   -------  stesso output  :  calendario - mese di giugno 2025





print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV   --  CALENDAR  setfirstweekday()   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")



import calendar

print('----- MESE set primo giorno week a SUNDAY - .setfirstweekday(calendar.SUNDAY)\n')
calendar.setfirstweekday(calendar.SUNDAY)  #  setta primo giorno del calendar
calendar.prmonth(2020, 12)

print('\n----- MESE set primo giorno week a MONDAY - .setfirstweekday(calendar.MONDAY)\n')
calendar.setfirstweekday(calendar.MONDAY)
calendar.prmonth(2025, 7)







print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV   --  CALENDAR  .weekday()   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")


import calendar
print(calendar.weekday(2020, 12, 24))

print(calendar.weekday(2025, 6, 26))  #  output : 3  (è mercoledì, lun = 0)








print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV   --  CALENDAR  weekheader()   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

#  solo header dei giorni

import calendar
print(calendar.weekheader(2))  #  argument (2) rappresenta la width (spazio tra i nomi dei giorni)

#  output : Mo Tu We Th Fr Sa Su
# tip : cambia la variare di .setfirstweekday  --  default > Mo









print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV -- CALENDAR  check bisestitico   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

#  True se bisestile


import calendar

print('Anno 2020 : ', calendar.isleap(2020))  #  2020 era bisestile >>> True
print('Anno 1984 : ', calendar.isleap(1984))  #  1984 era bisestile >>> True
print('Anno 1846 : ', calendar.isleap(1846))  #  False  1846 non bisestile

print('Q.tà anni bisestili dal 2010 al 2020(incluso) : ', calendar.leapdays(2010, 2021))
# not including 2021









print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV -- Calendar object   .iterweekdays() ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")


import calendar

c = calendar.Calendar(calendar.SUNDAY)
c.setfirstweekday(0)  #  (primo giorno della settimana impostato a lun =0)

for weekday in c.iterweekdays():  #  itera giorni della semana
    print(weekday, end=" ")

#  ----- output  :  0 1 2 3 4 5 6   (inizia da lun=0)









print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV -- Calendar object  .itermonthdates ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")



import calendar

c = calendar.Calendar()

print('\n-----  Itera luglio 2025  -- data odierna 26/6/2025\n')
for date in c.itermonthdates(2025, 7):  #  itera mese (al mom è il 26/6/2025)
    print(date, end=" ")


#   >>>  tip : l'output completerà sempre la settimana iniziale e finale



#  ----- output :  parte dall'ultimo giorno del mese precedente (30/6)
#                  fino al 3° dd del mese successivo

# 2025-06-30 2025-07-01 2025-07-02 2025-07-03 2025-07-04 2025-07-05 2025-07-06
# 2025-07-07 2025-07-08 2025-07-09 2025-07-10 2025-07-11 2025-07-12 2025-07-13
# 2025-07-14 2025-07-15 2025-07-16 2025-07-17 2025-07-18 2025-07-19 2025-07-20
# 2025-07-21 2025-07-22 2025-07-23 2025-07-24 2025-07-25 2025-07-26 2025-07-27
# 2025-07-28 2025-07-29 2025-07-30 2025-07-31 2025-08-01 2025-08-02 2025-08-03


print('\n\n----  Itera giugno 2025  -- data odierna 26/6/2025\n')
for date in c.itermonthdates(2025, 6):  #  itera mese (al mom è il 26/6/2025)
    print(date, end=" ")


#  ----- output :  parte dal mese precedente (dd 26/5)
#                  fino al 6° dd del mese successivo  (2025-07-06)


# 2025-05-26 2025-05-27 2025-05-28 2025-05-29 2025-05-30 2025-05-31 2025-06-01
# 2025-06-02 2025-06-03 2025-06-04 2025-06-05 2025-06-06 2025-06-07 2025-06-08
# 2025-06-09 2025-06-10 2025-06-11 2025-06-12 2025-06-13 2025-06-14 2025-06-15
# 2025-06-16 2025-06-17 2025-06-18 2025-06-19 2025-06-20 2025-06-21 2025-06-22
# 2025-06-23 2025-06-24 2025-06-25 2025-06-26 2025-06-27 2025-06-28 2025-06-29
# 2025-06-30 2025-07-01 2025-07-02 2025-07-03 2025-07-04 2025-07-05 2025-07-06










print("\n\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV -- Calendar object  .itermonthdays() ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

#   >>>  tip : l'output completerà sempre la settimana iniziale e finale
#              compensando con ' 0 '    (vedi output, - se necessario -
#                                        parte dal mese prec
#                                        sfora nel mese saccessivo)

import calendar

c = calendar.Calendar()

for iter in c.itermonthdays(2025, 6):
    print(iter, end=" ")




#  ------- output :

#   Maggio                               Giugno...
# 0 0 0 0 0 0       1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# ￪>lun 26/5        ￪> dom 1/6
#       ....Giugno                      Luglio
# 21 22 23 24 25 26 27 28 29 30       0 0 0 0 0 0
#                             ￪> lun             ￪> dom 6/luglio





print("\n\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  .itermonthdays2() ver II ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")



#  ritorna il mese sottoforma di tuple, anche iter2 compensa con gli '0'

for iter in c.itermonthdays2(2022, 8):
    print(iter, end=" ")


#   output : (1, 0) (2, 1) (3, 2) (4, 3) (5, 4) (6, 5) (7, 6) (8, 0) (9, 1)
#            (10, 2) (11, 3) (12, 4) (13, 5) (14, 6) (15, 0) (16, 1) (17, 2) (18, 3) (19, 4)
#            (20, 5) (21, 6) (22, 0) (23, 1) (24, 2) (25, 3) (26, 4) (27, 5) (28, 6) (29, 0)
#            (30, 1) (31, 2) (0, 3) (0, 4) (0, 5) (0, 6)








print("\n\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  .itermonthdays3()   ver III   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")



#  ritorna data completa sottoforma di tuple, iter3 compensa con i giorni mese succ e prec


for iter in c.itermonthdays3(2022, 8):
    print(iter, end=" ")

#  output : (2022, 8, 1) (2022, 8, 2) (2022, 8, 3) (2022, 8, 4)
#           (2022, 8, 5) (2022, 8, 6) (2022, 8, 7) (2022, 8, 8) (2022, 8, 9)
#           (2022, 8, 10) (2022, 8, 11) (2022, 8, 12) (2022, 8, 13) (2022, 8, 14)
#           (2022, 8, 15) (2022, 8, 16) (2022, 8, 17) (2022, 8, 18) (2022, 8, 19)
#           (2022, 8, 20) (2022, 8, 21) (2022, 8, 22) (2022, 8, 23) (2022, 8, 24)
#           (2022, 8, 25) (2022, 8, 26) (2022, 8, 27) (2022, 8, 28) (2022, 8, 29)
#           (2022, 8, 30) (2022, 8, 31) (2022, 9, 1) (2022, 9, 2) (2022, 9, 3) (2022, 9, 4)








print("\n\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  .itermonthdays4()   ver IV   ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")



#  tuples complete di anno, mese, giorno e weekday (integer)
#  compensa con data mese preced e sacc

for iter in c.itermonthdays4(2022, 2):
    print(iter, end=" ")


#  output : (2022, 1, 31, 0) (2022, 2, 1, 1) (2022, 2, 2, 2) (2022, 2, 3, 3)
#           (2022, 2, 4, 4) (2022, 2, 5, 5) (2022, 2, 6, 6) (2022, 2, 7, 0)
#           (2022, 2, 8, 1) (2022, 2, 9, 2) (2022, 2, 10, 3) (2022, 2, 11, 4)
#           (2022, 2, 12, 5) (2022, 2, 13, 6) (2022, 2, 14, 0) (2022, 2, 15, 1)
#           (2022, 2, 16, 2) (2022, 2, 17, 3) (2022, 2, 18, 4) (2022, 2, 19, 5)
#           (2022, 2, 20, 6) (2022, 2, 21, 0) (2022, 2, 22, 1) (2022, 2, 23, 2)
#           (2022, 2, 24, 3) (2022, 2, 25, 4) (2022, 2, 26, 5) (2022, 2, 27, 6)
#           (2022, 2, 28, 0) (2022, 3, 1, 1) (2022, 3, 2, 2) (2022, 3, 3, 3)
#           (2022, 3, 4, 4) (2022, 3, 5, 5) (2022, 3, 6, 6)








print("\n\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫￫￫￫  Mod IV -- Calendar object  .monthdays2calendar ￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")


# lun =0  --  dom =6
# ritorna una list di settimane(tuple)

import calendar

c = calendar.Calendar()

for data in c.monthdays2calendar(2025, 6):
    print(data)


#  output : [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
#           [(7, 0), (8, 1), (9, 2), (10, 3), (11, 4), (12, 5), (13, 6)]
#           [(14, 0), (15, 1), (16, 2), (17, 3), (18, 4), (19, 5), (20, 6)]
#           [(21, 0), (22, 1), (23, 2), (24, 3), (25, 4), (26, 5), (27, 6)]
#           [(28, 0), (29, 1), (30, 2), (31, 3), (0, 4), (0, 5), (0, 6)]









print("\n--------   MODULO 4  --  4.6.1.13 LAB: the calendar module --------\n")

# conteggio di un det giorno in un determinato anno
# es.  quanti lunedì (espresso in int) nell'anno xxxx

import calendar


class MyCalendar:

    def count_weekday_in_year(self, year, weekday):
        cal = calendar.Calendar()
        cnt = 0

        for m in range(1,13):
            cal_cust = cal.monthdays2calendar(year, m)

            for wk in cal_cust:   #  lista settimana
                for tupd in wk:  # lista tuple days
                    if (0, 0) <= tupd <= (0, 6): continue
                    if tupd == (weekday, weekday): cnt += 1
                    if (weekday, 0) <= tupd <= (weekday, 6): continue
                    else:
                         for dd in tupd:
                             if dd == weekday : cnt += 1
        return cnt



day = MyCalendar()

print('\nConteggio per 2019, q.tà lunedì = ', day.count_weekday_in_year(2019, 0))
#day.count_weekday_in_year(2019, 0)

print('\nConteggio per 2000, q.tà domeniche = ', day.count_weekday_in_year(2000, 6))
#day.count_weekday_in_year(2000, 6)

print('\nConteggio per 2020, q.tà venerdì = ', day.count_weekday_in_year(2020, 4))
#day.count_weekday_in_year(2020, 12)









print('\n\-----------------------------------------------------------\n')
print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫  PE 2 -- Mod IV  FINAL  TEST    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

#Q 7/16
#
# import os
#
# os.mkdir('C:/PycharmProjects/Py3/pictures')
# os.chdir('C:/PycharmProjects/Py3/pictures')
#
# os.mkdir('thumbnails')
# os.chdir('C:/PycharmProjects/Py3/pictures/thumbnails')
#
# os.mkdir('temp')
# os.chdir('../')  #  qui chdir imposta la root dir (C:..../Py3) come current⤵
# #                                                        ￬
# #                                                        ￬
# print('Echo root dir (dot-dot-slash): <', os.getcwd(), '>')  #  >>>>>     ➬➬     outpout : C:\PycharmProjects\Py3
#
#
# os.chdir('./')
# print('Echo dot-slash', os.getcwd())











print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫  PE 2 -- Mod IV  FINAL  TEST    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")

#Q 8/16

from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print('Echo data1 - data2 : ', date_1-date_2)   #   345 days, 0:00:00



print("\n▼↻  ￫￫￫￫￫￫￫￫￫￫￫  PE 2 -- Mod IV  FINAL  TEST    ￩￩￩￩￩￩￩￩￩￩￩ ↺▼\n")


def fun(n):
    s = '+'
    for i in range(n):
        #print('val di n = ', n)
        s += s
        yield s


for k in fun(2):
    print(k, end=' ')


#   ----output :  ++++++  (secondo giro del loop s == '++')
#                         ( quindi sarebbe '++'(loop 1) + (loop2)'++++'
#                          s = '++' >> s += s == '++++'



















