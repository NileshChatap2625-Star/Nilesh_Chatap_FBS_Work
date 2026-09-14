# num = int(input("Enter a number:"))

# temp = num
# count = 0

# while(temp > 0):
#     d = temp // 10
#     count += 1

# temp = num 
# count = 1

# while(temp > 0):
#     d = temp % 10
#     temp = temp // 10
#     sum = sum + (d ** count)

# if(sum == num):
#     print("Number is armstrong")
# else:
#     print("Number is not armstrong")


num = int(input("Enter a number: "))

n = num
digits = len(str(num))
total = 0

for i in range(digits):
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")