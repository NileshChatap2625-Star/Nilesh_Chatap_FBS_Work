# ####  type 1


# def strong():
#     num = int(input("Enter number:"))

#     n = num
#     temp = n
#     sum = 0

#     while(n > 0):
#         d = n % 10

#         fact = 1
#         for i in range(1, d+1):
#             fact = fact * i

#         sum = sum + fact
#         n = n // 10
#     if(temp == sum):
#         print("True")
#     else:
#         print("False")
    

# strong()


#### type 2



# def strong(num):
#     n = num
#     temp = n
#     sum = 0 

#     while(n > 0):
#         d = n % 10

#         fact = 1
#         for i in range(1, d+1):
#             fact = fact * i

#         sum = sum + fact
#         n = n // 10

#     if(temp == sum):
#         print("True")
#     else:
#         print("False")

# num = int(input("enter number:"))


# strong(num)




##### type 3


# def strong():
#     num = int(input("Enter a number:"))

#     n = num
#     temp = n
#     sum = 0

#     while(n > 0):
#         d = n % 10

#         fact = 1
#         for i in range(1, d+1):
#             fact = fact * i

#         sum = sum + fact
#         n = n // 10

#     if(temp == sum):
#         print("True")
#     else:
#         print("False")
    
# res = strong()
# print(res)




###### True 4



def strong(num):

    n = num
    temp = n
    sum = 0

    while(n > 0):
        d = n % 10

        fact = 1
        for i in range(1, d+1):
            fact = fact * i

        sum = sum + fact
        n = n // 10

    return temp == sum


num = int(input("Enter number:"))
   

res = strong(num)

print(res)
