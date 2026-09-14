# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)


import random
userID = input("Enter a userID:")
password = input("Enter a password:")

if(userID == 'Nitin' and password == 'Nitin123'):
    systemcap = random.randint(1000,10000)
    print(systemcap)
    Capture = int(input("Enter the Capture:"))
    if(Capture == systemcap):
        print("Successfully login")
    else:
        print("Invalid Capture")
else:
    print("Invalid userid and password")