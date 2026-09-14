## 7. Write a program to check if user has entered correct userid and password.

userID = input("Enter a userID:")
password = input("Enter a password:")

if(userID == 'Nilesh'  and password == 'Nilesh@123'):
    print("Correct, Welcome")
else:
    print("Not correct, Please try again")