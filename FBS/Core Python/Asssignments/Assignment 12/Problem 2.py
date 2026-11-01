string = input("Enter a string: ")
index = int(input("Enter the index of the character to remove: "))

new_string = string[:index] + string[index + 1:]
print("Original string:", string)
print("Modified string:", new_string)