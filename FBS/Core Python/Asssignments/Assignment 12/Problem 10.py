string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

count1 = 0
count2 = 0

for char in string1:
    count1 += 1
for char in string2:
    count2 += 1

if count1 > count2:
    print("The first string is longer.")
elif count1 < count2:
    print("The second string is longer.")
else:
    print("Both strings are of equal length.")