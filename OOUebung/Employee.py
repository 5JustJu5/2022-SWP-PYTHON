from enum import Enum
from Person import person

class position(Enum):
    Mitarbeiter = 1
    Abteilungsleiter = 2
    CIO = 3


class employee(person):
    
    def __init__(self, vorName, nachName, gender, salary, position):
        super().__init__(vorName, nachName, gender)
        self.salary = salary
        self.position = position


    def __str__(self):
        return super().__str__() + " " + str(self.salary) + " " + str(self.position.name)
        

