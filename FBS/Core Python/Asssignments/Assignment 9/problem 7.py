def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)

n = int(input("enter a number:"))
res = sum_digits(n)
print("sum of digits=", res)