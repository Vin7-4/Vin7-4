################################################################################################

#######################        C L A S S E S

##################################################################################################


#  Classes & Objects

#  Class : definisce il progetto generale : ad essa si associano set di attributes e methods

#  Object : istanza associata alla class, può avere il suo valore unico.




class PcSummary:
    def __init__(self, brand, mouse, keyb, monitor):  # funzione che inizializza la class
        self.brand = brand
        self.mouse = mouse  # objects  >>> Protected attribute
        self.keyb = keyb
        self.monitor = monitor

    def smry_pc(self):  # funzione che definisce la presentazione
        print(f"Brand pc : {self.brand}\nTipo device di puntamento : {self.mouse}\n"
              f"Tastiera : {self.keyb}\nMonitor : {self.monitor}")


pc_smry1 = PcSummary('ASUS', 'RAZER DeathAdder v2', 'SteelSeries -(it)', 'HP OMEN 16:9 120hz - EneClass=B+')
pc_smry1.smry_pc()
#
# -1.
# Definiamo
# l
# 'inizializzazione della class con un method apposito (__init__) :
#
#
# class [< * Nome
#
#
# class >]:  # nome della class ha sempre la prima lettera grande
#
#
#     def __init__(self, obj1, obj2...
#
# )
# self.obj1 = obj1
# self.obj2 = obj2
#
# -2.
# di
# solito
# impostiamo
# una
# funzione
# di
# presentazione
# con
# un
# print:
# (in questo caso sfruttiamo l'encapsulation)
#
#
# def [ <
#
#
#     nome
# function > (self)]:
# print(f"Nome : {self.obj1} - Età : {self.obj2}") << < ENCAPSULATION

# >>>  tecnicamente definiamo l'output della class


# -3.
# utilizziamo
# la
#
#
# class per eseguire code custom:
#
#
# --ex1
#
# +++  [ <
# *Nome
#
#
# class >] = Impiegato
#
# var1 = Impiegato([nome], [età])
#
# >> > utilizziamo la var con un method (che avrà il nome della def con encapsulation - sfruttiamo il print)
#
# [< nome function > (self)] = display
#
# var1.display()


class Impiegatizio:
    def __init__(self, nome, age, ufficio):  # inizialzza la class con questa particolare funzione
        self.nome = nome
        self.__age = age  # Private attribute : non può essere utilizzata come method (esiste .nome ma NON .age)
        self.ufficio = ufficio

    def uff_imp(self):  # questa funzia può essere utilizzata come method
        print(f"Nome : {self.nome} - Età : {self.__age}  --  Ufficio : {self.ufficio}")


imp_uff = Impiegatizio("Alice", 25, '5A/3')  # associo ad una var la class coi parametri

imp_uff.uff_imp()  # esegue la (class)funzione con i print di presentazione

# >> >> >> output: Nome: Alice - Età: 25 - -  Ufficio: 5
# A / 3

imp_uff.ufficio = input("\nDio porco Alice ha cambiato ufficio... inserisci nuovo ufficio di destinazione ?>_ ")
imp_uff.uff_imp()

# >> >> > '.nome'
# e
# '.ufficio'
# possono
# essere
# utilizzati
# come
# methods
# "esterni"
# '.age'
# non
# può
# essere
# utilizzato in tal
# senso
# perchè
# è
# private
# attribute
# (si utIlizza il double underscore >> self.__age)

print('\n⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈')
print("------------------   LAB® personal™   --------------------♆")
print('⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇\n')


class Soccer:
    def __init__(self, nome, age, ruolo):
        self.nome = nome
        self.age = age
        self.ruolo = ruolo

    def display(self):
        print(f"\n INFO PERSONALI ATLETA -- Nome : {self.nome} - Età : {self.age} | Ruolo = {self.ruolo}")


# immettiamo parametri custom
play1 = Soccer(nome=input("Immetti nome atleta ?>_ "), age=input("Immetti età atleta ?>_ "),
               ruolo=input("Immetti ruolo atleta ?>_ "))
play1.display()


######################################################################################## INHERITANCE


class Veicoli:
    def start_eng(self): print("Start engine! Bruuum")


class Auto(Veicoli): pass


k = Auto()
k.start_eng()

#  >> >> output: Start
# engine! Bruuum


class Persona:
    gen = 'Maschio'  # lo utilizziamo come method della var con il cmd >>> print(x.gen)

    def __init__(self, nome):
        self.__cl_nome = nome
        print("Nome : ", nome)  # dalla def in basso in poi ognuna erediterà il nome (self.__cl_nome)

    def eyes_col(self): print(f"{self.__cl_nome} ha gli occhi celesti (sì ma d'estate però)")

    def birth(self, a): print(f"{self.__cl_nome} - Età : ", a, "anni")

    def altz(self, h): print(f"In tutto ciò, {self.__cl_nome} è alto ", h + 'm')


x = Persona('Enzo')
x.eyes_col()
x.birth('43')
x.altz('1,78')
print(x.gen)

print('\n------------\n')

y = Persona('Alice')
y.birth('25')
y.altz('1,90')




print('\n⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈⏈')
print("♆--------------   LAB® personal™   ----------------♆")
print('⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇⏇\n')



class Animali:
    def __init__(self, n):
        self.n = n

    def scream(self):
        pass


class Cane(Animali):
    def scream(self): return "Bark (sono un chihuhua)"


class Gatto(Animali):
    def scream(self): return "Miaooooo"


do = Animali(Cane)
ga = Gatto(Gatto)

print(do.scream())
print(ga.scream())




##########################################################################  POLIMORFISMO



class Bird:
    def scream(self): return 'Tweetuuuu'


a1 = [Cane("Krull"), Gatto("RedSonic"), Bird()]  # utilizza la lista con le class come elementi
# (anche di tipo differente)

for a in a1: print(a.scream())  # e le stampa utilizzando un loop

# >> > output:
#
# Bark(sono
# un
# chihuhua)
# Miaooooo
# Tweetuuuu

from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for heading in soup.find_all('h2'):
            print(heading.text)
    except requests.RequestException as e:
        print(f"Error: {e}")


scrape_website('https://example.com')






































