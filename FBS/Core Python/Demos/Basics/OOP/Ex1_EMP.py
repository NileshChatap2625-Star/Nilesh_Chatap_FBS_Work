from abc import ABC,abstractmethod
class Employee:
    def __init__(self,id1,name1,sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id
    def setId(self,newid):
        self.id = newid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal
    def setSal(self, newsal):
        self.sal = newsal

    @abstractmethod
    def CalSal(self):
        pass

    def __str__(self):
        return f"Id = {self.id}\tName = {self.name}\tSalary = {self.sal}"
    
    def display(self):
        print(f"Id = {self.id}\tName = {self.name}\tSalary = {self.sal}")


class HR(Employee):
    def __init__(self, id1, name1, sal1, comission):
        super().__init__(id1, name1, sal1)
        self.comission = comission

    def getcomission(self):
        return self.comission
    def setcomission(self, newcomission):
        self.comission = newcomission

    def CalSal(self):
        print(f"final sal of HR = {self.sal+self.comission}")

    def __str__(self):
        return super().__str__() + f"\tComission = {self.comission}"
    
    def display(self):
        print(f"Comission={self.comission}\t")
        return super().display()


#### Hr end here

class Devloper(Employee):
    def __init__(self, id1, name1, sal1, bonus):
        super().__init__(id1, name1, sal1)
        self.bonus = bonus

    def getbonus(self):
        return self.bonus
    def setbonus(self, newbonus):
        self.bonus = newbonus

    def CalSal(self):
        print(f"Final sal of devloper is = {self.sal+self.bonus}")

    def __str__(self):
        return super().__str__() + f"\tBonus = {self.bonus}"

    def display(self):
        print(f"Bonus={self.bonus}\t")
        return super().display()


# e1 = Employee(1, 'Rahul', 3535)
h1 = HR(7,'hima', 2525, 1500)
d1 = Devloper(9, 'ram', 1546, 2500)

# h1.CalSal()
# e1.CalSal()
# d1.CalSal()

# print(e1)
print(h1)
print(d1)