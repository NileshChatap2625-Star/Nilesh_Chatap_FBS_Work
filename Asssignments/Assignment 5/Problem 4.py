start = int(input("Enter start number:"))
end = int(input("Enter end number:"))


for n in range(start, end+1):
    temp = n
    total = 0
    digits = len(str(n))

    while(temp > 0):
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10
    if(total == n):
        print(n)

