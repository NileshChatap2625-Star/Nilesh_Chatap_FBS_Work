class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def getmake(self):
        return self.make
    def setmake(self, newmake):
        self.make = newmake

    def getmodel(self):
        return self.model
    def setmodel(self, newmodel):
        self.model = newmodel

    def getyear(self):
        return self.year
    def setyear(self, newyear):
        self.year = newyear

    def __str__(self):
        return f"Year = {self.year}\t Model = {self.model}\t Make = {self.make}"

    def display(self):
        print(f"Year = {self.year}\t Model = {self.model}\t Make = {self.make}")

class BMW(Car):
    def __init__(self, make, model, year, series):
        super().__init__(make, model, year)
        self.series = series

    def getseries(self):
        return self.series
    def setseries(self, newseries):
        self.series = newseries

    def __str__(self):
        return super().__str__() + f"\t series = {self.series}"

    def display(self):
        super().display()
        print(f"Series = {self.series}")

class Audi(Car):
    def __init__(self, make, model, year, trim):
        super().__init__(make, model, year)
        self.trim = trim

    def gettrim(self):
        return self.trim
    def settrim(self, newtrim):
        self.trim = newtrim

    def __str__(self):
        return super().__str__() + f"\t trim = {self.trim}"

    def display(self):
        super().display()
        print(f"Trim = {self.trim}")

c1 = Car('Toyota', 'Camry', 2020)
b1 = BMW('BMW', 'X5', 2021, 'M')
a1 = Audi('Audi', 'A4', 2022, 'Premium')

# c1.display()
# b1.display()
# a1.display()

print(c1)
print(b1)
print(a1)