def sum(num):
    sum = 0
    for i in range(1, num + 1):
        if(num % i == 0):
            sum += i
    print("sum of prime number=", sum)

num = int(input("Enter a number:"))

sum(num)