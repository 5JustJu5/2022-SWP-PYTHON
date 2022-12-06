from Gender import gender

class person:

    def __init__(self,vorName, nachName, gender):
        self.vorName = vorName
        self.nachName = nachName
        self.gender = gender
        
    


    def __str__(self):
        return self.vorName + " " + self.nachName + " " + str(self.gender.name)



        




