n = int(input("Enter a number:"))

temp = n
sum = 0

while(temp > 0):
    d = temp % 10

    fact = 1
    for i in range(1, d + 1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10

if(sum == n):
    print("Number is strong number")
else:
    print("Number is not strong")




#### for practices


# n = int(input("enter number:"))

# temp = n
# sum = 0

# while(temp > 0):
#     d = temp % 10

#     fact = 1
#     for i in range(1, d + 1):
#         fact = fact * i

#     sum = sum + fact
#     temp = temp // 10

# if(sum == n):
#     print("strong")
# else:
#     print("not strong")