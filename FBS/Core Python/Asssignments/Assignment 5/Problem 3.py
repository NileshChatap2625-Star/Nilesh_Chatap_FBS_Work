passenger = int(input("Enter number of passenger:"))
ticket = int(input("Enter ticket:"))

sum = 0

for i in range(1, passenger+1):
    age = int(input("Enter age:"))

    if(age < 12):
        discount = ticket - (ticket * 30 / 100 )
    elif(age > 59):
        discount = ticket - (ticket * 50 / 100 )
    else:
        discount = ticket
    print("ticket=", discount)
    sum = sum + discount
print("Total_Amount=", sum)
