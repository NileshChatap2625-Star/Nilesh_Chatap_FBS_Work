## TAke input of 3 digit

num = int(input("Enter 3 digit number:"))

a = num // 100
b = (num // 10) % 10
c = num % 10

## Perform addition

sum = a + b + c
print("Sum of three digits:", sum)

