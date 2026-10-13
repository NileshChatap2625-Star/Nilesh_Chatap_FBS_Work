class Student:
    def __init__(self,name1, mark1, department1):
        self.name = name1
        self.mark = mark1
        self.department = department1

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name = newname

    def getMark(self):
        return self.mark
    def setMark(self, newmark):
        self.mark = newmark

    def getDepartment(self):
        return self.department
    def setDepartment(self,newdepartment):
        self.department = newdepartment

    def __str__(self):
        return f"Name = {self.name}\t Mark = {self.mark}\t Department = {self.department}" 
    
    def display(self):
        print(f"Name = {self.name}\t Mark = {self.mark}\t Department = {self.department}")

class Science(Student):
    def __init__(self, name1, mark1, department1, Bio_mark1):
        super().__init__(name1, mark1, department1)
        self.Bio_mark = Bio_mark1

    def getBioMark(self):
        return self.Bio_mark

    def setBioMark(self, newBio_mark):
        self.Bio_mark = newBio_mark

    def __str__(self):
        return super().__str__() + f"\t Bio_mark = {self.Bio_mark}"
    
    def display(self):
        super().display()
        print(f"Bio Mark = {self.Bio_mark}")


class Arts(Student):
    def __init__(self, name1, mark1, department1, History_mark1):
        super().__init__(name1, mark1, department1)
        self.History_mark = History_mark1

    def getHistoryMark(self):
        return self.History_mark

    def setHistoryMark(self, newHistory_mark):
        self.History_mark = newHistory_mark

    def __str__(self):
        return super().__str__() + f"\t History_mark = {self.History_mark}"

    def display(self):
        super().display()
        print(f"History Mark = {self.History_mark}")

s1 = Student('Alice', 85, 'Science')
S1 = Science('Alice', 85, 'Science', 90)
A1 = Arts('Alice', 85, 'Arts', 88)

# s1.display()
# S1.display()
# A1.display()

print(s1)
print(S1)
print(A1)