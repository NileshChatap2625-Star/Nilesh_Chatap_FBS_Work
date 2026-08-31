num = int(input("enter number:"))

reverse = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)


if(num == reverse):
    print("Number is palindrome")
else:
    print("Number is not palindrome")



#     #### OR

# num = int(input("enter number:"))

# temp = num
# rev_num = 0

# while(temp > 0):
#     d = temp % 10
#     temp = temp // 10
#     rev_num = rev_num * 10 + d
# if(num == rev_num):
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")


### fsctorial sum

# num = int(input("enter number:"))


# temp = num
# sum = 0

# while(temp > 0):
#     d = temp % 10
#     temp = temp // 10
#     fact = 1
#     for i in range(1, d + 1):
#         fact = fact * i
#     sum = sum + fact

# if(sum == num):
#     print("Number is strong number")
# else:
#     print("Number is not strong")


####  Amstrong number

# num = int(input("enter number:"))

# temp = num
# count = 0

# while(temp > 0):
#     count += 1
#     d = temp // 10

# temp = num
# num = 0

# while(temp > 0):
#     d = temp % 10
#     temp = temp // 10
#     sum = sum + (d ** count)

# if(sum == num):
#     print(f'{num} is an armstrong number')
# else:
#     print(f'{num} is not armstrong number')


    
