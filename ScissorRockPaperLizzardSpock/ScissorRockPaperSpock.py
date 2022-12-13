import random
import sqlite3
from sqlite3 import Error
from tabulate import tabulate






def format(answers,ans):
    com = ""
    if answers[0] == 0:
        com = "Schere"
        print("Schere")
    if answers[0] == 1:
        com = "Stein"
        print("Stein")
    if answers[0] == 2:
        com = "Papier"
        print("Papier")
    if answers[0] == 3:
        com = "Echse"
        print("Echse")
    if answers[0] == 4:
        com = "Spock"
        print("Spock")
    
    print("vs")

    player = ""
    if answers[1] == 0:
        player = "Schere"
        print("Schere")
    if answers[1] == 1:
        player = "Stein"
        print("Stein")
    if answers[1] == 2:
        player = "Papier"
        print("Papier")
    if answers[1] == 3:
        player = "Echse"
        print("Echse")
    if answers[1] == 4:
        player = "Spock"
        print("Spock")
        
    win = ""   
    if ans == 1:
        win = "Gewonne"
        print("Gewonne")
    if ans == 2:
        win = "Verloren"
        print("Verloren")
    if ans == 3:
        win = "Unentschieden"
        print("Unentschieden")

    return player,com,win

def evaluation(answers):
    if answers[0] == answers[1]:
        return 3
    if answers[0] == 0:
        if answers[1] == 1 or answers[1] == 4:
            return 1
        return 2
    if answers[0] == 1:
        if answers[1] == 2 or answers[1] == 4:
            return 1
        return 2
    if answers[0] == 2:
        if answers[1] == 0 or answers[1] == 3:
            return 1
        return 2
    if answers[0] == 3:
        if answers[1] == 0 or answers[1] == 1:
            return 1
        return 2
    if answers[0] == 4:
        if answers[1] == 2 or answers[1] == 3:
            return 1
        return 2

def reverseEvolution(player):
    if player == 0:
        return 1
    if player == 1:
        return 2
    if player == 2:
        return 0
    if player == 3:
        return 1
    if player == 4:
        return 2


def inputs(input1,switch, analyse, list):
    com1 = smartCom(switch, analyse, list)
    player1 = list[input1-1]
    if switch == 3:
        com1 = player1
    if switch == 4:
        com1 = reverseEvolution(player1)

    
    return com1,player1

def mode(sheldon):
    #0 --> Schere
    #1 --> Stein
    #2 --> Papier
    #3 --> Echse
    #4 --> Spock

    list = []
    if sheldon:
        for i in range(5):
            list.append(i)
    else:
        for i in range(3):
            list.append(i)
    return list


def stats(player,com,winner):
    zwischenPlayer = dictoPlayer.get(player)
    zwischenCom = dictoCom.get(com)
    zwischen = dicto.get(winner)
  
    zwischen = zwischen + 1
    zwischenCom = zwischenCom+1
    zwischenPlayer = zwischenPlayer+1

    dicto.update({winner:zwischen})
    dictoPlayer.update({player:zwischenPlayer})
    dictoCom.update({com:zwischenCom})

    


def analyse(switch, dicto,dictoPlayer):
    played = dicto.get(1) + dicto.get(2) + dicto.get(3)
    probPlayer = []
    probCom = []
    probWinP = []
    for i in range(5):
        probPlayer.append(dictoPlayer.get(i)/played)
        probCom.append(dictoCom.get(i)/played)
   
    for i in range(1,4):
        probWinP.append(dicto.get(i)/played)
    
    if switch:
        print("Probability Player:")
        print("| Schere: " + str(probPlayer[0]) + "| Stein: " + str(probPlayer[1]) + "| Papier: " + str(probPlayer[2]) + "| Echse: " + str(probPlayer[3]) + "| Spock: " + str(probPlayer[4]) + "\n")
        print("Probability Computer:")
        print("| Schere: " + str(probCom[0]) + "| Stein: " + str(probCom[1]) + "| Papier: " + str(probCom[2]) + "| Echse: " + str(probCom[3]) + "| Spock: " + str(probCom[4]) + "\n")
        print("Probability win:")
        print("| Gewonnen: " + str(probWinP[0]) + "| Verloren: " + str(probWinP[1]) + "| Papier: " + str(probWinP[2]) + "\n")

    return probPlayer

def smartCom(switch,ana,list):
   

    if switch == 1:
        com = random.randint(0,len(list)-1)
        com1 = list[com-1]
        return com1
    elif switch == 2:   
        probPlayer = analyse(ana)
        problist = []
        comList = []

    
        for i in probPlayer:
            problist.append(int(i*10000))

        for i in range(5):
            for y in range(problist[i]):
                comList.append(i)

        com = random.randint(0,len(comList)-1)
        com1 = comList[com-1]
        return com1

#
#
#
#
#
##
#
#
#
#
#
#
#Datenbanbanek
#
#
#
#
#
#
#
#
#



#Datenbank erstellen 
def datBase():
    conn = sqlite3.connect('datas.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE usersInteger
            (ID INT PRIMARY KEY     NOT NULL,
            player           int    NOT NULL,
            com              int    NOT NULL,
            winner           int     NOT NULL);''')
    print("Table created successfully")


    conn.close()


#Insert in beiden DBs
def insertVaribleIntoTable(player, com, winner,player2,com2,winner2):
    try:
        sqliteConnection = sqlite3.connect('datas.db')
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")
        
        sqlite_select_query2 = """SELECT * from usersInteger"""

        cursor.execute(sqlite_select_query2)
        records = cursor.fetchall()
        if len(records)-1 < 0:
            id = 1
        else:
            id = records[len(records)-1][0]+1

        sqlite_insert_with_param = """INSERT INTO usersInteger
                          (id, player, com, winner) 
                          VALUES (?, ?, ?, ?);"""
        data_tuple = (id, player2, com2, winner2)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


#Die IntegerDatenbank auslesen
def insertIntoDicto(switch):
    try:
        sqliteConnection = sqlite3.connect('datas.db')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT * from usersInteger"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        if switch:
            listen = []
            for row in records:
                listen.append("ID: ")
                listen.append(str(row[0]))
                listen.append("player: ")
                listen.append(str(row[1]))
                listen.append("com: ")
                listen.append(str(row[2]))
                listen.append("winner: ")
                listen.append(str(row[3]))
                listen.append("|||||")
            print(tabulate(records, headers=["id","player","com","winner"]))
            return str(listen)
        else:
            for row in records:
                player = row[1]
                com = row[2]
                winner = row[3]
                stats(player,com,winner)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()





if __name__ == '__main__':
    #datBase()
    dictoPlayer = {0:0,1:0,2:0,3:0,4:0}
    dictoCom = {0:0,1:0,2:0,3:0,4:0}
    dicto = {1:0,2:0,3:0}

    insertIntoDicto(False)
    print(dictoPlayer)
    print(dictoCom)
    print(dicto)
    print("\n")

    exit = True

    schwierigkeit = 1
    while exit:
        input2 = int(input("1. play 2. difficulty 3.Stats 6. Beenden"))
        
        while input2 == 1:
            input1 = int(input("waehlen sie ihre Figur [1.Schere 2.Stein 3.Papier 4.Echse 5.Spock 6.Beenden]"))
            if input1 == 6:
                print("beendet")
                input2 = "jjj"
            else:
                list = mode(True)
                answers = inputs(input1,schwierigkeit,False,list)
       
                #print(answers)
                ans = evaluation(answers)
                datas = format(answers,ans)
                insertVaribleIntoTable(datas[0],datas[1],datas[2],answers[1],answers[0],ans)

        while input2 == 2:
            schwierigkeit = int(input("1. Normal 2. Schwierig 3. Unentschieden 4.Unmöglich"))
            input2 = "jjj"

        if input2 == 3:
            insertIntoDicto(True)
            input2 = "jjj"
        
        if input2 == 6:
            print("Beendet")
            exit = False
        
        
               
        
       
