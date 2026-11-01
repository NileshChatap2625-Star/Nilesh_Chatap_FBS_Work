
from abc import ABC, abstractmethod

class Vehical(ABC):
    def __init__(self, cNo, colour):
        self.cno = cNo
        self.colour = colour

    def getCno(self):
        return self.cno

    def setCno(self, newNO):
        self.cno = newNO

    def getcolour(self):
        return self.colour

    def setcolour(self, newcolour):
        self.colour = newcolour

    @abstractmethod
    def brake(self):
        pass

    def __str__(self):
        return f"Che No = {self.cno}, Colour = {self.colour}"


class Car(Vehical):
    def brake(self):
        print("This is the Brake of Car")


c = Car(12, 'red')
print(c)
c.brake()
