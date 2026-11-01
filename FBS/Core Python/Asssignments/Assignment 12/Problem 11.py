string = input("Enter a string: ")

new_string = ""

for char in string:
    if char == " ":
        new_string += "_"
    else:
        new_string += char

print("Original string:", string)
print("Modified string:", new_string)