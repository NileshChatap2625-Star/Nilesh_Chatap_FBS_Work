list = [1, 10, 7, 5, 3, 12, 16, 20]

new_list = []

for list in list:
    if list % 2 != 0:
        new_list.append(list)

print("Original list:", list)
print("List of odd numbers:", new_list)