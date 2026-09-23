##### type 1


def prime():

    num = int(input("Enter number:"))

    if(num % 2 == 0):
        print("False")
    else:
        print("True")
    
prime()





###### type 2


# def prime(num):
#     if(num % 2 == 0):
#         print("False")
#     else:
#         print("True")

# num = int(input("enter number:"))


# prime(num)




##### type 3



# def prime():
#     num = int(input("Enter a number:"))
#     flag = True

#     if(num  % 2 == 0):
#         flag = False
        
        
#     return flag
# res = prime()
# print(res)



##### type 4


def prime(num):
    flag = True

    if(num % 2 == 0):
        flag = False

    return flag

num = int(input("Enter number:"))
   

res = prime(num)

print(res)
