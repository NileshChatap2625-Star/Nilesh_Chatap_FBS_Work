gender = input("Enter gender (M/F):")
age = int(input("Enter age:"))


if(gender == "F"):
    if(age >= 18):
        print("Girl is eligible for marriage.")
    else:
        print("Pahle padhai kar lo.")
else:
    if(age >= 21):
        print("Boy is eligible for marriage.")
    else:
        print("Pahle kama le.")
        