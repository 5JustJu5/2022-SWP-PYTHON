import random




def format(answers,ans):
    if answers[0] == 0:
        print("Schere")
    if answers[0] == 1:
        print("Stein")
    if answers[0] == 2:
        print("Papier")
    if answers[0] == 3:
        print("Echse")
    if answers[0] == 4:
        print("Spock")
    
    print("vs")

    if answers[1] == 0:
        print("Schere")
    if answers[1] == 1:
        print("Stein")
    if answers[1] == 2:
        print("Papier")
    if answers[1] == 3:
        print("Echse")
    if answers[1] == 4:
        print("Spock")
        
    if ans == 1:
        print("Gewonne")
    if ans == 2:
        print("Verloren")
    if ans == 3:
        print("Unentschieden")

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
    
    pass


def inputs(list):
    com = random.randint(0,len(list)-1)
    com1 = list[com-1]
    input1 = int(input("waehlen sie ihre Figur [1.Schere 2.Stein 3.Papier 4.Echse 5.Spock]"))
    player1 = list[input1-1]
    
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


def stats(dictoPlayer,dictoCom,dicto,ans,answers):
    zwischenPlayer = dictoPlayer.get(answers[1])
    zwischenCom = dictoPlayer.get(answers[0])
    zwischen = dicto.get(ans)
    
    zwischen = zwischen + 1
    zwischenCom = zwischenCom+1
    zwischenPlayer = zwischenPlayer+1

    dicto.update({ans:zwischen})
    dictoPlayer.update({answers[1]:zwischenPlayer})
    dictoCom.update({answers[0]:zwischenCom})


if __name__ == '__main__':
    dictoPlayer = {0:0,1:0,2:0,3:0,4:0}
    dictoCom = {0:0,1:0,2:0,3:0,4:0}
    dicto = {1:0,2:0,3:0}
    while True:    
        list = mode(True)
        answers = inputs(list)
        ans = evaluation(answers)
        stats(dictoPlayer,dictoCom,dicto,ans,answers)
        print(dictoCom)
        print(dictoPlayer)
        print(dicto)
        format(answers,ans)
