class Bike:
    def __init__(self, name1,number,speed):
        self.name = name1
        self.number = number
        self.speed = speed

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name = newname

    def getNumber(self):
        return self.number
    def setNumber(self, newnumber):
        self.number = newnumber

    def getSpeed(self):
        return self.speed
    def setSpeed(self, newspeed):
        self.speed = newspeed

    def __str__(self):
        return f"Name = {self.name}\t Number = {self.number}\t Speed = {self.speed}"

    def display(self):
        print(f"Name = {self.name}\t Number = {self.number}\t Speed = {self.speed}")

class SportsBike(Bike):
    def __init__(self, name1, number, speed, turbo):
        super().__init__(name1, number, speed)
        self.turbo = turbo

    def getTurbo(self):
        return self.turbo
    def setTurbo(self, newturbo):
        self.turbo = newturbo

    def __str__(self):
        return super().__str__() + f"\t turbo = {self.turbo}"
  

    def display(self):
        super().display()
        print(f"Turbo = {self.turbo}")

class CruiserBike(Bike):
    def __init__(self, name1, number, speed, comfort):
        super().__init__(name1, number, speed)
        self.comfort = comfort

    def getComfort(self):
        return self.comfort
    def setComfort(self, newcomfort):
        self.comfort = newcomfort

    def __str__(self):
        return super().__str__() + f"\t comfort = {self.comfort}"

    def display(self):
        super().display()
        print(f"Comfort = {self.comfort}")

b1 = Bike('Yamaha', '1234', 120)
s1 = SportsBike('Suzuki', '5678', 150, 'Yes')
c1 = CruiserBike('Honda', '9101', 100, 'High')

# b1.display()
# s1.display()
# c1.display()

print(b1)
print(s1)
print(c1)