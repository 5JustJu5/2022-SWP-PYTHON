from operator import itemgetter, mod
import random
from re import L
from string import capwords
from wsgiref.headers import tspecials



def pokerKarten(ziehung):
    #list = ["A","K","Q","J",10,9,8,7,6,5,4,3,2]
    list = []
    for i in range(2,15):
        list.append(i)
    kartenDeck = []
    for i in range(ziehung):
        kartenDeck = kartenDeck+list
    #print(kartenDeck)
    return kartenDeck

def deal_cards(cards):
    check1 = []
    while len(check1) < 5:
        zahl = random.randint(0,len(cards)-1)
        if(zahl not in check1):
            check1.append(zahl)
    #print(check1)
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
    sortlistcards = sorted(listcards, key=itemgetter(0))
    return sortlistcards




def di(cards):
    dicto = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0}
    for i in range(len(cards)):
        stats(dicto,cards[i][0])
    sorted_dicto = dict(sorted(dicto.items(), key=lambda item:item[1], reverse=True))
    return sorted_dicto


def royalFlush(cards):
    #Selbe Farbe?
    for i in range(len(cards)):
        #print(cards)
        if cards[0][1] != cards[i][1]:
            return False
    if (cards[len(cards)-1][0] - cards[0][0]) == 4 and cards[len(cards)-1][0] == 14:
        #print(cards)
        #print(cards[len(cards)-1][0])
        return True
    return False

def straighFlush(cards):
    for i in range(len(cards)):
        #print(cards)
        if cards[0][1] != cards[i][1]:
            return False
    if (cards[len(cards)-1][0] - cards[0][0]) == 4:
        #print(cards)
        #print(cards[len(cards)-1][0])
        return True
    return False

def FourOfAKind(cards):
    sorted_dicto = di(cards)
    value_dicto = list(sorted_dicto.values())[0]
    if value_dicto == 4:
        #print(cards)
        return True
    return False

def fullHouse(cards):
    sorted_dicto = di(cards)
    value_dicto1 = list(sorted_dicto.values())[0]
    value_dicto2 = list(sorted_dicto.values())[1]
    card = list(sorted_dicto)[0]
    if value_dicto1 == 3 and value_dicto2 == 2 and card == 14:
        #print(cards)
        return True
    return False

def flush(cards):
    for i in range(len(cards)):
        #print(cards)
        if cards[0][1] != cards[i][1]:
            return False
    #print(cards)
    return True


def straight(cards):
    sorted_dicto = di(cards)
    value_dicto1 = list(sorted_dicto.values())[0]
    if (cards[len(cards)-1][0] - cards[0][0]) == 4 and value_dicto1 < 2:
        #print(cards)
        #print(cards[len(cards)-1][0] - cards[0][0])
        return True
    return False

def threeOfAKind(cards):
    sorted_dicto = di(cards)
    value_dicto = list(sorted_dicto.values())[0]
    if value_dicto == 3:
        #print(cards)
        return True
    return False

def twoPair(cards):
    sorted_dicto = di(cards)
    value_dicto1 = list(sorted_dicto.values())[0]
    value_dicto2 = list(sorted_dicto.values())[1]
    if value_dicto1 == 2 and value_dicto2 == 2:
        #print(cards)
        return True
    return False

def pair(cards):
    sorted_dicto = di(cards)
    value_dicto1 = list(sorted_dicto.values())[0]
    if value_dicto1 == 2:
        #print(cards)
        return True
    return False

def highCard(cards):
    card = cards.pop()
    return True
    
    





def stats(dicto, name):
    zwischen = dicto.get(name)
    zwischen = zwischen +1
    dicto.update({name:zwischen})

def allocation(dicto,cards):
    if royalFlush(cards):
        stats(dicto, "Royal Flush")
        return True
    if straighFlush(cards):
        stats(dicto,"Straight Flush")
        return True
    if FourOfAKind(cards):
        stats(dicto,"Four of a Kind")
        return True
    if fullHouse(cards):
        stats(dicto,"Full House")
        return True
    if flush(cards):
        stats(dicto,"Flush")
        return True
    if straight(cards):
        stats(dicto,"Straight")
        return True
    if threeOfAKind(cards):
        stats(dicto,"Three of a Kind")
        return True
    if twoPair(cards):
        stats(dicto,"Two Pair")
        return True
    if pair(cards):
        stats(dicto,"Pair")
        return True
    if highCard(cards):
        stats(dicto,"High Card")
        return True


def prop(dicto1,dicto2,range2):
    list2 = list(dicto1.values())
    for i in range(len(list2)):
        result = (list2[i]/range2)*100
        dicto2.update({i:result})
    print(dicto2)







    


if __name__ == '__main__':
    dicto = {"Royal Flush":0,"Straight Flush":0,"Four of a Kind":0,"Full House":0,"Flush":0,"Straight":0,"Three of a Kind":0,"Two Pair":0,"Pair":0, "High Card":0}
    dicto2 = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    cards = pokerKarten(4)
    #listcards = deal_cards(cards)
    #print(street(listcards))


    for i in range(1000000):
        listcards = deal_cards(cards)
        allocation(dicto, listcards)
    prop(dicto,dicto2,1000000)
    print(dicto)

   
    
