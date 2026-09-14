
# ###### Type 1


# def armstrong():
#     num = int(input("Enter number:"))

#     n = num
#     temp = n
#     sum = 0

#     while(n > 0):
#         d = n % 10
#         sum = sum + (d ** 3)
#         n = n // 10

#     if(sum == num):
#         print("True")
#     else:
#         print("False")

# armstrong()




##### Type 2 


# def armstrong(num):
#     n = num
#     temp = n
#     sum = 0

#     while(n > 0):
#         d = n % 10
#         sum = sum + (d ** 3)
#         n = n // 10

#     if(sum == num):
#         print("True")
#     else:
#         print("False")

# num = int(input("enter number:"))


# armstrong(num)





####### Type 3



# def armstrong():
#     num = int(input("Enter a number:"))

#     n = num
#     temp = n
#     sum = 0

#     while(n > 0):
#         d = n %10
#         sum = sum + (d ** 3)
#         n = n // 10

#     return sum == num

# res = armstrong()
# print(res)






##### type 4


def armstrong(num):
    n = num
    temp = n
    sum = 0

    while(n > 0):
        d = n % 10
        sum = sum + ( d ** 3)
        n = n // 10

    return sum == num

num = int(input("Enter a number:"))


res = armstrong(num)

print(res)
