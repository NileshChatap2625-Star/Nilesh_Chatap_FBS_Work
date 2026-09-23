##### type 1


# def pallindrome():

#     num = int(input("Enter number:"))
#     n = num
#     temp = n
#     r = 0

#     while(n > 0):
#         d = n % 10
#         r = r * 10 + d
#         n = n // 10

#     if(temp == r):
#         print("True")
#     else:
#         print("False")

# pallindrome()



##### type 2


    
# def pallindrome(num):
#     n = num
#     r = 0
#     temp = n

#     while(n > 0):
#         d = n % 10
#         r = r * 10 + d
#         n = n // 10

#     if(temp == r):
#         print("True")
#     else:
#         print("False")

# num = int(input("enter number:"))


# pallindrome(num)



#### type 3
    


# def pallindrome():
#     num = int(input("Enter a number:"))

#     n = num
#     r = 0
#     temp = n

#     while(n > 0):
#         d = n % 10
#         r = r * 10 + d
#         n = n // 10

#     return temp == r
    

    
# res = pallindrome()
# print(res)




##### type 4


def pallindrome(num):
    n = num
    r = 0
    temp = n

    while(n > 0):
        d = n % 10
        r = r * 10 + d
        n = n // 10

    return temp == r

    
num = int(input("Enter number:"))
   

res = pallindrome(num)

print(res)
