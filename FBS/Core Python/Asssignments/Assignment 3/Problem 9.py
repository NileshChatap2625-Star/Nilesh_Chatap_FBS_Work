# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

Math = int(input("Enter marks:"))
Science = int(input("Enter marks:"))
English = int(input("Enter marks:"))
Marathi = int(input("Enter marks:"))
Hindi = int(input("Enter marks:"))

sum = Math + Science + English + Marathi + Hindi

grade = sum / 5
print(grade)

if(grade > 75):
    print("First Class")
elif(grade > 40):
    print("Second Class")
else:
    print("Fail")