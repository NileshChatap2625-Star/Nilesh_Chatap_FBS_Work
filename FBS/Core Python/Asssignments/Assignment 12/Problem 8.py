string = input("Enter a string: ")

new_string = ""

for i in range(0, len(string), 2):
    new_string += string[i]

print("Original string:", string)
print("Modified string:", new_string)