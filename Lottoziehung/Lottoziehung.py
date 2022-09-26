from ast import main
import random
from unittest.main import MAIN_EXAMPLES

moeglich = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
stats = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,33:0,
            34:0,35:0,36:0,37:0,38:0,39:0,40:0,41:0,42:0,43:0,44:0,45:0}

            
def ziehung(gezogen):
    ziehungen = 1
    while ziehungen <= gezogen:
        zahl = random.randint(0,len(moeglich)-ziehungen)
        #print(zahl)
        #print("|")
        print(moeglich[zahl])
        statistik(moeglich[zahl])

        zwischen = moeglich[zahl]
        zwischen2 = moeglich[len(moeglich)-ziehungen]
        moeglich[zahl] = zwischen2
        moeglich[len(moeglich)-ziehungen] = zwischen
        ziehungen = ziehungen +1
    print("done")
        

def statistik(zahl):
    zwischen = stats.get(zahl)
    zwischen = zwischen +1
    stats.update({zahl:zwischen})
    


if __name__ == '__main__':
    k = 0
    while k <= 1000:
        ziehung(6)
        k = k+1
    print(stats)
    