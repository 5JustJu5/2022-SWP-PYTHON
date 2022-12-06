from Person import person
from Departments import departments
from Departments import wichtigkeit
from Company import company
from Employee import employee
from Employee import position
from Gender import gender


if __name__ == '__main__':
    p1 = person("Julian","Schmid",gender.men)
    p2 = person("Erik","Schmoelzer",gender.men)
    p3 = person("Michael","Zechner",gender.men)
    p4 = person("Lena","Mayer",gender.women)
    p5 = person("Paula","lechner",gender.women)
    p6 = person("Theresa","Muster",gender.women)
    e1 = employee(p1.vorName,p1.nachName,p1.gender,6000,position.CIO)
    e2 = employee(p2.vorName,p2.nachName,p2.gender,1500,position.Abteilungsleiter)
    e3 = employee(p3.vorName,p3.nachName,p3.gender,2500,position.Abteilungsleiter)
    e4 = employee(p4.vorName,p4.nachName,p4.gender,900,position.Mitarbeiter)
    e5 = employee(p5.vorName,p5.nachName,p5.gender,1500,position.Mitarbeiter)
    e6 = employee(p6.vorName,p6.nachName,p6.gender,1200,position.Mitarbeiter)


    einkauf = departments("Einkauf", [e3,e6], wichtigkeit.Wichtig)
    vertrieb = departments("Vertrieb", [e4,e5,e1], wichtigkeit.Essenziell)
    marketing = departments("Marketing", [e2], wichtigkeit.Unwichtig)

    abteilungen = [einkauf, vertrieb, marketing]
    c1 = company("HTL",abteilungen)

    c1.howMany()
    c1.howManyDepartments()
    c1.whichDepartment()
    c1.menAndWomen()