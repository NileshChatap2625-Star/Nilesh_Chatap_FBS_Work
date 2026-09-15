num = int(input("enter a number:"))

sum = 0
fact = 1
for i in range(1, num+1):
    fact = fact * i
    sum = sum + (i / fact)
print(sum)