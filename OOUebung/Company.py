from Employee import employee
from Departments import departments
from Employee import employee


class company:
    def __init__(self,firmenName, departmentss):
        self.firmenName = firmenName
        self.departmentss = departmentss

    def __str__(self):
        zw = []
        for i in self.departmentss:
            zw.append(str(i))
        return self.firmenName + " " + str(zw)

    def howMany(self):
        mitarbeiter = 0
        abteilungsleiter = 0
        cio = 0
        for i in self.departmentss:
            for e in i.employees:
                if e.position.value == 1:
                    mitarbeiter = mitarbeiter+1
                if e.position.value == 2:
                    abteilungsleiter = abteilungsleiter+1
                if e.position.value == 3:
                    cio = cio+1
        print("Mitarbeiter: " + str(mitarbeiter) + " Abteilungsleiter: " + str(abteilungsleiter) + " CIO: " + str(cio))
        return mitarbeiter, abteilungsleiter, cio

    def howManyDepartments(self):
        print("Es gibt " + str(len(self.departmentss)) + " Abteilungen im Unternehmen")
        return len(self.departmentss)

    def whichDepartment(self):
        zw = 0
        pfusch = 0
        pfusch2 = 0
        for i in self.departmentss:
            pfusch = pfusch +1

            #print(len(i.employees))
            if len(i.employees) > zw:
                zw = len(i.employees)
                pfusch2 = pfusch
        print(self.departmentss[pfusch2-1].name + " |Mitabreiter: " + str(zw))
        return self.departmentss[pfusch2-1].name,str(zw)

    def menAndWomen(self):
        men = 0
        gesamt = 0
        for i in self.departmentss:
            for e in i.employees:
                gesamt = gesamt +1
                if e.gender.value == 1:
                    men = men +1
        proMen = (men/gesamt)*100
        proWomen = 100-proMen
        print("FrauenAnteil: " + str(proWomen) + "% " + "MaennerAnteil " + str(proMen) + "%")
        return proMen,proWomen
        
      
        
        
        

            


    