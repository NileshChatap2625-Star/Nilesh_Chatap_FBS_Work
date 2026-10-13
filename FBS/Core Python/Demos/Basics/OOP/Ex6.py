class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def getBrand(self):
        return self.brand
    def setBrand(self, newbrand):
        self.brand = newbrand

    def getModel(self):
        return self.model
    def setModel(self, newmodel):
        self.model = newmodel

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price = newprice

    def __str__(self):
        return f"Brand = {self.brand}\t Model = {self.model}\t Price = {self.price}"

    def display(self):
        print(f"Brand = {self.brand}\t Model = {self.model}\t Price = {self.price}")

class GamingLaptop(Laptop):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def getGPU(self):
        return self.gpu
    def setGPU(self, newgpu):
        self.gpu = newgpu

    def __str__(self):
        return super().__str__() + f"\t gpu = {self.gpu}"

    def display(self):
        super().display()
        print(f"GPU = {self.gpu}")

class Ultrabook(Laptop):
    def __init__(self, brand, model, price, weight):
        super().__init__(brand, model, price)
        self.weight = weight

    def getweight(self):
        return self.weight 
    def setweight(self, newweight):
        self.weight = newweight

    def __str__(self):
        return super().__str__() + f"\t weight = {self.weight}"

    def display(self):
        super().display()
        print(f'Weight = {self.weight}')

l1 = Laptop('Dell', 'Inspiron', 800)
g1 = GamingLaptop('Asus', 'ROG', 1500, 'NVIDIA RTX 3060')
u1 = Ultrabook('Apple', 'MacBook Air', 1200, 1.25)

# l1.display()
# g1.display()
# u1.display()

print(l1)
print(g1)
print(u1)