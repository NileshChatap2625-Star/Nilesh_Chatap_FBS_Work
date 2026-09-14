### star pattern

# for i in range(1,6):                  #---------> row change
#     for j in range(1,6):              # --------> collumn change
#         print('*', end = ' ')           # print change
#     print()





### for collumn change

# for i in range(1,6):                  #---------> row change
#     for j in range(1,6):              # --------> collumn change
#         print(j, end = ' ')           # print change
#     print()




#### for row change

# for i in range(1,6):                  #---------> row change
#     for j in range(1,6):              # --------> collumn change
#         print(i, end = ' ')           # print change
#     print()



### for alphabet

# for i in range(0, 5):
#     for j in range(0, 5):
#         print(chr(65 + i), end = ' ')
#     print()


# for i in range(0, 5):
#     for j in range(0,5):
#         print(chr(65 + i), end = ' ')
#     print()


# for i in range(1, 6):
#     print(" " * (5 - i), end =' ')
#     for j in range(i):
#         print(i, end = ' ')
#     print()


# for i in range(5, 0, -1):
#     print((i - 1) * " ", end = ' ')
#     for j in range(i):
#         print(i, end = ' ')
#     print()


# for i in range(1, 6):                                     
#     for j in range(5, 5-i,):      ## for j in range(i+1)
#         print(j, end = ' ')
#     print()

### same 

# for i in range(1, 6):
#     print("* " * i)
# print()



# for i in range(5, 0, -1):
#     for j in range(i):
#         print('*', end= ' ')
#     print()


# for i in range(5, 1):
#     for j in range(5, i-1):
#         print(j, end= ' ')
#     print()


# for i in range(5, 0, -1):                                     
#     for j in range(i):      ## for j in range(i+1)
#         print('*', end = ' ')
#     print()

# for i in range(1, 6):
#     for j in range(i, 7-1):
#         print("*", end= ' ')
#     print()

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end= ' ')
    print()

