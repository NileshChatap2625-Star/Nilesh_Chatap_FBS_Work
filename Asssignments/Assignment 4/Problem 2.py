#### print old number up to n

n = int(input("Entter a number:"))

for i in range(1, n):
    if(i % 2 != 0):
        print(i)