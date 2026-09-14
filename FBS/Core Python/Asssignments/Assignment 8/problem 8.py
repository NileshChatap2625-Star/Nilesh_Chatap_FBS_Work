def revers():
    num = int(input("Enter a number:"))
    r = 0

    while(num > 0):
        d = num % 10
        r = r * 10 + d
        num = num // 10

    print("revers number=", r)

revers()