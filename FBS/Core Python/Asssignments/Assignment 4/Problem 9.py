# num = int(input("Enter a number :"))

# for i in range(1, num + 1):
#     if(num % i == 0):
#         print(i)


###  OR 

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
n = int(input("Enter the given number: "))

for i in range(start, end + 1):
    if i % n == 0:
        print(i)