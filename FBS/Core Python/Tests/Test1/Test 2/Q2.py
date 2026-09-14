number = int(input("Enter a three digit number: "))

number1 = number // 100
number2 = (number // 10) % 10
number3 = number % 10

if number1 == 2 * number2 and number1 == number3 / 2:
    print("yes, you have done it")
else:
    print("please try again")
     