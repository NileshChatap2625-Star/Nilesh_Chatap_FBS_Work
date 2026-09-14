def sum_digits(num):
    sum = 0
    while(num > 0):
        d = num % 10
        sum = sum + d
        num = num // 10
    print("sum of digits=", sum)

num = int(input("Enter a number:"))
res = sum_digits(num)
print(res)