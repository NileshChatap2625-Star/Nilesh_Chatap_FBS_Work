### perfect number

n = int(input("Enter a number:"))

sum = 0

for i in range(1, n):
    if(n % i == 0):
        sum += 1
    print(i)

if(sum == n):
    print("Number is perfect")
else:
    print("Number is not perfect")