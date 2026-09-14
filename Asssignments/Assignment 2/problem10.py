## Take input 

num = int(input("Enter 3 digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

reverse_num = c * 100 + b * 10 + a
print("Reverse of the number is:", reverse_num)