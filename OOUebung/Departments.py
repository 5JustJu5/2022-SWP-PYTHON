from enum import Enum
from Employee import employee

class wichtigkeit(Enum):
    Unwichtig = 1
    Durschnitt = 2
    Wichtig = 4
    Essenziell = 5
    


class departments:
    def __init__(self, name, employees, wichtigkeit):
        self.name = name
        self.employees = employees
        self.wichtigkeit = wichtigkeit

    def __str__(self):
        zw = []
        for i in self.employees:
            zw.append(str(i))
        return self.name+ " " + str(zw) + " " + str(self.wichtigkeit.name) 

