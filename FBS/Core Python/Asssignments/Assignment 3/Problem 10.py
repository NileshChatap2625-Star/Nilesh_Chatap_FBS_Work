#10. Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

gender = input("Enter gender:")
age = int(input("Enter age:"))


if(gender == 'F'):
    if(age >= 18):
        print("Girls are eligible for marride")
    else:
        print("Girls are not eligible for marride")
else:
    if(age >= 21):
        print("Boys are eligible for marride")
    else:
        print("Boys are not eligible for marride")




    

