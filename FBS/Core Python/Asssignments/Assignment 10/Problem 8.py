list = [10, 20, 30, 40]

new_list = []

for i in list:
    new_list.append(i)

print("Orignal list=", list)
print("Duplicate list= ", new_list)

new_list[0] = 100
new_list[1] = 90

print("After changing duplicate list:")

print("Orignal list=", list)
print("Duplicate list =", new_list)