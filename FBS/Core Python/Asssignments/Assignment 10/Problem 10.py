list = [ 10, 20, 30, 10, 40, 50]

num = int(input("Enter element to remove :"))

new_list = []

for i in list:
    if i != num:
        new_list.append(i)
        
print("List =", new_list)