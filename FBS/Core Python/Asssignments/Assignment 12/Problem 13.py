string = input("Enter a string: ")

digit = 0
letter = 0

for char in string:
    if char.isdigit():
        digit += 1
    elif char.isalpha():
        letter += 1

print("Number of digits in the string:", digit)
print("Number of letters in the string:", letter)