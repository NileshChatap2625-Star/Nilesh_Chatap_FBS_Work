def armstrong(num):
    sum = 0
    temp = num
    while(temp > 0):
        d = temp % 10
        sum = sum + d ** 3
        temp = temp // 10

    if(num == sum):
        print(f"{num} is armstrong number")
    else:
        print(f"{num} is not armstrong number")

num = int(input("Enter a number:"))
res = armstrong(num)
print(res)