n = int(input("enter a number:"))


for i in range(2, n):
    if(n % i == 0):
        print("Number is prime")
        break
else:
    print("Number is not prime")
     





### find prime number in 1 to 100

n = int(input("enter a number:"))

for num in range(1, n+1):
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        print(num, end =' ')





    
    



