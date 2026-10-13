class Student:
    stcount = 0
    def __init__(self, FRN, name, BName):
        self.FRN = FRN
        self.name = name
        self.BName = BName
        Student.stcount += 1

    def display(self):
        print(f"FRN = {self.FRN}\t Name = {self.name}\t BName = {self.BName}")

class Placedstudent(Student):
    def __init__(self, FRN, name, BName, Company):
        super().__init__(FRN, name, BName)
        self.Company = Company
        
    def setCompany(self, company):
        self.Company = company
    def getCompany(self):
        return self.Company
    def display(self):
        print(f"Company = {self.Company}")
        super().display()

s1 = Student(18, 'Nilesh', 'FBS')
s2 = Student(19, 'Rohit', 'FBS')
s3 = Student(20, 'Nitin', 'FBS')
s4 = Placedstudent(20, 'Raj', 'FBS', 'TCS')
s5 = Placedstudent(20, 'Ravi', 'FBS', 'TCS')

print("Total number of students:", Student.stcount)