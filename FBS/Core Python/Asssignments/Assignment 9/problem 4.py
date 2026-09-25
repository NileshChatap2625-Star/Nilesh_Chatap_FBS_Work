def sum(num):
    if num == 0:
        return 0
    else:
        return num + sum(num - 1)


num = int(input("enter a number:"))

res = sum(num)
print("sum of numbers=", res)