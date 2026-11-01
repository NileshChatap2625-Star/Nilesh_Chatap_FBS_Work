class Emp:
    def __int__(self,id,name,sal):
        self.__id = id
        self.__name = name
        self.__sal = sal

    def getid(self):
        return self.__id
    def setid(self, newid):
        self.__id = newid

    def __str__(self):
        return f"Id = {self.__id} Name = {self.__name} Sal = {self.__sal}"

e1 = Emp(12,'nilesh', 1212)
e1.getid()
print(e1.getid())
print(e1)