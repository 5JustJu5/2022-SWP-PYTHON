class ListElement:
    
    def __init__(self, obj):
        self.obj = obj
        self.nextelement = None

    def __str__(self):
        return self.obj



class EinfachVerketteteListe:
    
    def __init__(self):
        self.startElem = ListElement(1)

    def getLastelem(self):
        le = self.startElem
        while le.nextelement != None:
            le = le.nextelement
        return le

    # def delete(self, o):
    #     le = self.startElem
    #     while (le.nextelement != None) and (le.obj != o):
    #         zw = le.nextelement
    #         if zw == o:
    #             zw2 = zw.nextelement
    #             if zw != None:
    #                 le.nextelement = zw2
    #             else:
    #                 le.nextelement == None
    #                 break
    #     le = le.nextelement
        
            

    def addLast(self, o:int):
        newElem = ListElement(o)
        lastElem = self.getLastelem()
        lastElem.nextelement = newElem

    def writeList(self):
        le = self.startElem
        while le != None:
            print(le.obj)
            le = le.nextelement

if __name__ == "__main__":
    l1 = EinfachVerketteteListe()
    l1.addLast(2)
    l1.addLast(10)
    #l1.delete("hund")
    l1.writeList()





