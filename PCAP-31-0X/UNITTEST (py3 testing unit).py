
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
#                                      ---------------------------------------------------

#                                                      TESTING(con UNITTEST)

#                                      ---------------------------------------------------
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *




#                             Package utilizzato per testare linee di codice           (methods, functions, classes...)




# ------------------------------       Tipi di TESTING principali  (dal livello più basso a quello più grande)  :


# 1. UNIT TESTING : è il livello più basso di testing
# unit testing è il check/test della singola riga o porzione funzionale di codice  (method, functions...)


# 2. INTEGRATION TESTING
# testing di una det parte software (abbastanza grande, per un team) di una determinata application


# 3. FUNCTIONAL TESTING (END-TO-END TEST)
# ha la portata di testing più ampia
# il codice viene testato rispetto alle specifiche funzionali e ai requisiti dell'applicazione software


###############################################################################################################




#   ---  test di una semplice class


from math import pi


def area_of_circle(r):
    return pi * (r ** 2)

#  let's try   (altrimenti l'importing rimane triste)

area_of_circle(5)

# >>>  salviamo questa class come " areacircle.py " nella dir degli scripts

# --------     n.b.
# >>> area_of_circle(5)
#         78.53981633974483


#               ---------------------------------------------        stiliamo una unit test con unittest




import unittest
from areacircle import area_of_circle     #       << << qui importerà la def " area_of_circle " da " areacircle.py "
from math import pi




class Test_AoC(unittest.TestCase):
    def testAoC(self):
        self.assertAlmostEqual(area_of_circle(1),
                               pi)  # >>>  prende la funzia (area_of_circle) le assegna un dato ( ' (1) ' ) e lo confronta con il secondo dato ( ' pi ' )
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(3.5), pi * 3.5 ** 2)

    if __name__ == '__main__':  #      >>>  la presenza di queste due righe di codice permette di lanciare il test
        unittest.main()  #          >>>  usando il nome del file py di test salvato successivamente (test_areacircle.py) come eseguibile

#    >>>   si salva il tutto con il nome  " test_areacircle.py "     ( nella stessa dir di " areacircle.py " )
#                                                                                         ovviamente per convenzione si usano rif simili


#      >>>>>>>>      si lancia il test    (da console py3)

#      test_areacircle.py

#                   oppure     python -m unittest test_areacircle.py

# (copia/incolla da PyCharm)
















