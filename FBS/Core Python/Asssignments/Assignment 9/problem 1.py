#### sum of series using recursive function

def fact(n):
    if(n==0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

def sum_of_series(n):
    if(n == 0):
        return n
    else:
        return fact(n) + sum_of_series(n-1)

n = int(input("enter a number:"))

res = sum_of_series(n)
print("sum_if_series=", res)