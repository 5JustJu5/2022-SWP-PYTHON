

class ListElement:
    
    def __init__(self, obj):
        self.obj = obj
        self.nextelement = None

    def setNextElement(self,nextelement):
        self.nextElement = nextelement

    def getNextElem(self):
        return self.nextElement

    def getObj(self):
        return self.obj


    