list = [10, 20, 10, 30, 20, 40, 70, 50]

new_list = []

for i in list:
    found = False

    for j in new_list:
        if i == j:
            found = True
            break

    if found == False:
        new_list.append(i)

print("List after removing duplicates =", new_list)