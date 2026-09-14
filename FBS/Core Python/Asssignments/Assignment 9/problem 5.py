def fact(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of number =", fact)

num = int(input("Enter a number:"))
res = fact(num)
print(res)