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

    def delete(self, o):
         le = self.startElem
         while (le.nextelement != None) and (le.obj != o):
            zw = le.nextelement
            if zw.obj == o:
                zw2 = zw.nextelement
                if zw2 != None:
                    le.nextelement = zw2
                else:
                    le.nextelement = None
                    break
            le = le.nextelement

    def insertAfter(self, previtem, newItem):
        pointerElement = self.startElem
        while pointerElement != None and pointerElement.obj != previtem:
            if pointerElement.nextelement == None:
                return False
            else:
                pointerElement = pointerElement.nextelement
        
        newElem = ListElement(newItem)
        nextElem = pointerElement.nextelement
        pointerElement.nextelement = newElem
        newElem.nextelement = nextElem

    def find(self,o):
        le = self.startElem
        while le != None:
            if le.obj == o:
                return True
            le = le.nextelement
        return False

    def length2(self):
        le = self.startElem
        count = 0
        while le.nextelement != None:
            le = le.nextelement
            count += 1
        return count 

    def index2(self, o):
        le = self.startElem
        count = 0
        while le != None:
            if le.obj == o:
                return count
            le = le.nextelement
            count += 1
        return False

    def deleteAfterIndex(self, count):
        le = self.startElem
        for i in range(count-1):
            if le.nextelement == None:
                return False
            else:
                le = le.nextelement
        le.nextelement = None
            
        
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
    l1.addLast(100)
    l1.addLast(4)
    l1.insertAfter(2,2222)
    l1.deleteAfterIndex(4)
    print(l1.index2(100))
    #print(l1.length2())
    #l1.delete(2)
    print(l1.find(2))
    print("hallo")
    l1.writeList()





