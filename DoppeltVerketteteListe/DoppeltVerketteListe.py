class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.nextelement = None
        self.previuselement = None

class Arraylist:
    def __init__(self):
        self.elements = []

    def append(self, obj):
        self.elements.append(obj)

    def insertt(self, obj, pos):
        self.elements.insert(pos, obj)

    def delete(self,obj):
        self.elements.remove(obj)

    def index(self, obj):
        return self.elements.index(obj)
    
    def pop(self, pos):
        return self.elements.pop(pos)
    
    def sort(self, pos):
        self.elements.sort()

class DoublyLinkedList:
    def __init__(self):
        self.arraylist = Arraylist()
        self.head = None
        self.tail = None

    def addAfter(self, obj):
        self.arraylist.append(obj)
        new_node = ListElement(obj)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previuselement = self.tail
            self.tail.nextelement = new_node
            self.tail = new_node

    def insert(self, obj, position):
        new_node = ListElement(obj)
        self.arraylist.insertt(obj, position)

        if self.head is None:
            if position == 0:
                self.head = new_node
                self.tail = new_node
        else:
            current = self.head

            if position == 0:
                new_node.nextelement = self.head
                self.head.previuselement = new_node
                self.head = new_node
            else:
                for i in range(position - 1):
                    if current.nextelement is None:
                        break
                    current = current.nextelement

                new_node.previuselement = current
                new_node.nextelement = current.nextelement
                if current.nextelement is not None:
                    current.nextelement.prev = new_node
                else:
                    self.tail = new_node
                current.nextelement = new_node
        

    def delete(self, obj):
        self.arraylist.delete(obj)
        current = self.head
        found = False
        while current is not None:
            if current.obj == obj:
                found = True
                if current.previuselement is not None:
                    current.previuselement.next = current.nextelement
                else:
                    self.head = current.nextelement
                if current.nextelement is not None:
                    current.nextelement.prev = current.previuselement
                else:
                    self.tail = current.previuselement
                break
            current = current.nextelement
        if found == False:
            print("Dieses Element existiert wurde nicht gefunden")

    def index(self, obj):
        #print(self.arraylist.index(obj))
        current = self.head
        index = 0

        while current is not None:
            if current.obj == obj:
                return index
            current = current.nextelement
            index += 1

    def pop(self, position):
        current = self.head
        self.arraylist.pop(position)
        if position is None or position == 0:
            data = self.head.obj
            self.head = self.head.nextelement

            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

            return data
        else:
            for i in range(position):
                current = current.nextelement

            data = current.obj

            if current.previuselement is not None:
                current.previuselement.next = current.nextelement
            if current.nextelement is not None:
                current.nextelement.prev = current.previuselement
            else:
                self.tail = current.previuselement

            return data

    def insertion_sort(self):
        if self.head is None:
            return

        sorted_list = DoublyLinkedList()
        current = self.head

        while current is not None:
            next_node = current.nextelement
            current.previuselement = None
            current.nextelement = None

            if sorted_list.head is None:
                sorted_list.head = current
                sorted_list.tail = current
            else:
                sorted_current = sorted_list.head
                while sorted_current is not None and current.obj > sorted_current.obj:
                    sorted_current = sorted_current.nextelement

                if sorted_current is None:
                    sorted_list.tail.nextelement = current
                    current.previuselement = sorted_list.tail
                    sorted_list.tail = current
                elif sorted_current.previuselement is None:
                    current.nextelement = sorted_list.head
                    sorted_list.head.previuselement = current
                    sorted_list.head = current
                else:
                    sorted_current.previuselement.next = current
                    current.previuselement = sorted_current.previuselement
                    sorted_current.previuselement = current
                    current.nextelement = sorted_current

            current = next_node

        self.head = sorted_list.head
        self.tail = sorted_list.tail

    def writeList(self):
        current = self.head
        while current is not None:
            print(current.obj, end=" - ")
            current = current.nextelement
        print("None")

dll = DoublyLinkedList()
dll.addAfter(20)
dll.insert(5,0)
dll.insertion_sort()
dll.insert(6,0)
dll.index(20)
dll.pop(2)
#dll.delete(20)
dll.writeList() 
dll.writeList() 
print(dll.arraylist.elements)


