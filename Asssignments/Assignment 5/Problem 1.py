
for i in range(3):
    user_name = input("Enter user_name:")
    password = input("Enter password:")

    if(user_name == 'Nilesh' and password == 'Nilesh123'):
        print("Successfully login")
        break
    else:
        print("Invalid user_name and password")
else:
    print("attempt 3 is over now your account is baned")