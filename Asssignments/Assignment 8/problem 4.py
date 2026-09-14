def sum():
    num = int(input("Enter a number:"))
    sum = 0

    for i in range(1, num + 1):
        if(i % 2 != 0):
            sum += i
    print("sum of odd numbers=", sum)

sum()