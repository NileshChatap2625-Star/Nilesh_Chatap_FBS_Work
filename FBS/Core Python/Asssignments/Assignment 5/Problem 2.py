student = int(input("Number of students:"))

total_percentage = 0

for i in range(1, student+1):
    print("Student", i)

    total = 0

    for j in range(1,6):
        marks = float(input("Enter Marks of subject " + str(j) + ": "))
        total = total + marks

    percentage = total / 5

    print("Percentage=", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / student 
print("Average_percentage=", average)



