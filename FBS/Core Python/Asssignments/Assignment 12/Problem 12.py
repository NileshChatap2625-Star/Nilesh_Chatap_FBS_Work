string = input("Enter a string: ")

count = 0

for char in string:
    if char > "a" and char < "z":
        count += 1

print("Number of lowercase letters:", count)