list = [10, 20, 30, 40, 50, 60, 70]

m = int(input("Enter a number:"))
n = int(input("Enter a number:"))

for i in list:
    if(i % m == 0 and i % n == 0):
        print(i)