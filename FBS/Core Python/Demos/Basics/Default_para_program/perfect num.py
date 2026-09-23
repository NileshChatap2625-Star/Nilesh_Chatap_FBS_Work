# ###### Type 1

# def perfect():

#     num = int(input("Enter a number: "))

#     sum = 0
#     for i in range(1, num):
#         if(num % i == 0):
#             sum = sum + i
#     if(sum == num):
#         print("True")
#     else:
#         print("False")

# perfect()




###### type 2



# def perfect(num):
#     sum = 0
#     for i in range(1, num):
#         if(num % i == 0):
#             sum = sum + i

#     if(sum == num):
#         print("True")
#     else:
#         print("False")

# num = int(input("Enter a number: "))

# perfect(num)





########## type 3


# def perfect():
#     num = int(input("Enter a number: "))

#     sum = 0
#     for i in range(1, num):
#         if(num % i == 0):
#             sum = sum + i
#     if(sum == num):
#         return True
#     else:
#         return False

# res = perfect()
# print(res)





##### type 4 


def perfect(num):
    sum = 0
    for i in range(1, num):
        if(num % i == 0):
            sum = sum + i
    return sum == num

num = int(input("Enter a number: "))

res = perfect(num)
print(res)