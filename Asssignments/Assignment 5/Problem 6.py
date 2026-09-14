n = int(input("Enter how prime number:"))

count = 0
num = 2

while(count < n):
    factorrs = 0 

    for i in range(1, num+1):
        if(num % i == 0):
            factorrs = factorrs + 1

    if(factorrs == 2):
        print(num)
        count = count + 1

    num = num + 1
