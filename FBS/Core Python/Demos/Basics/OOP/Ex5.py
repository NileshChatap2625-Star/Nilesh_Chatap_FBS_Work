class city:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getPopulation(self):
        return self.population
    def setPopulation(self, newpopulation):
        self.population = newpopulation

    def __str__(self):
        return f"Name = {self.name}\t Population = {self.population}"

    def display(self):
        print(f"Name = {self.name}\t Population = {self.population}")

class Dubai(city):
    def __init__(self, name, population, tourism):
        super().__init__(name, population)
        self.tourism = tourism

    def getTourism(self):
        return self.tourism
    def setTourism(self, newtourism):
        self.tourism = newtourism

    def __str__(self):
        return super().__str__() + f"\t tourism = {self.tourism}"

    def display(self):
        super().display()
        print(f"Tourism = {self.tourism}")

class NewYork(city):
    def __init__(self, name, population, finance):
        super().__init__(name, population)
        self.finance = finance

    def getFinance(self):
        return self.finance
    def setFinance(self, newfinance):
        self.finance = newfinance

    def __str__(self):
        return super().__str__() + f"\t finance = {self.finance}"
 
    def display(self):
        super().display()
        print(f"Finance = {self.finance}")

c1 = city('Generic City', 1000000)
d1 = Dubai('Dubai', 3000000, 'High')
n1 = NewYork('New York', 8000000, 'Very High')

# c1.display()
# d1.display()
# n1.display()

print(c1)
print(d1)
print(n1)