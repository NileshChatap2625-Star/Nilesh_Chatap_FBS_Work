def revers(num):
    r = 0

    while(num > 0):
        d = num % 10
        r = r * 10 + d
        num = num // 10
    return r

num = int(input("Enter a number:"))
res = revers(num)
print("revers number=", res)