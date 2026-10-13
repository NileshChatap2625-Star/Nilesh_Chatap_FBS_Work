class student:
    BName = 'FBS'
    @staticmethod
    def setBName(Newname):
        student.BName = Newname

    def __init__(self, name, frn, batch, BName):
        self.name = name
        self.frn = frn
        self.batch = batch
        self.BName = BName

    # def getName(self):
    #     return self.name
    # def setName(self, newname):
    #     self.name = newname

    # def getFRN(self):
    #     return self.frn
    # def setFRN(self, newfrn):
    #     self.frn = newfrn

    # def getBatch(self):
    #     return self.batch
    # def setBatch(self, newbatch):
    #     self.batch = newbatch

    # def getBName(self):
    #     return self.BName
    # def setBName(self, newBName):
    #     self.BName = newBName

    def display(self):
        print(f"Name = {self.name}\t FRN = {self.frn}\t Batch = {self.batch}\t BName = {student.BName}")

# s1 = student('Nilesh', 18, '24-JUNE', 'FBS')
# s2 = student('Rohit', 19, '24-JUNE', 'FBS')
# s3 = student('Nitin', 20, '24-JUNE', 'FBS')
# s1.display()
# s2.display()
# s3.display()
print(student.BName)
student.setBName("Firstbit solution")
print(student.BName)


