## not divided in 2,3

n = int(input("Enter a number:"))

for i in range(1, n+1):
    if(i % 2 != 0 and i % 3 != 0):
        print(i)