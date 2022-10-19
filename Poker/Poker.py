from operator import mod
import random
from string import capwords



def pokerKarten(ziehung):
    list = ["A","K","Q","J",10,9,8,7,6,5,4,3,2]
    kartenDeck = []
    for i in range(ziehung):
        kartenDeck = kartenDeck+list
    #print(kartenDeck)
    return kartenDeck

def deal_cards(cards):
    check1 = []
    while len(check1) < 5:
        zahl = random.randint(0,5)
        if(zahl not in check1):
            check1.append(zahl)
    #funktioniert
    #check2 = [3,16,29,42]
    
    listcards = []
    for i in range(5):
        listbetw = []
        n1 = cards[check1[i]]
        n2 = check1[i] % 4
        listbetw.append(n1)
        listbetw.append(n2)
        listcards.append(listbetw)
    return listcards



if __name__ == '__main__':
    cards = pokerKarten(4)
    listcards = deal_cards(cards)
    print(listcards)

   
    
