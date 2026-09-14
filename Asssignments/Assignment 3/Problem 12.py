### Number is palindrome or not

num = int(input("Enter number:"))

if(num < 100 or num > 999):
    print("Please enter a 3 digit number")
else:
    reverse = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)

if(num == reverse):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")