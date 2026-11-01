string = input("Enter a string: ")

count = 0

for char in string:
    if char in "aeiouAEIOU":
        count += 1

print("Number of vowels in the string:", count)