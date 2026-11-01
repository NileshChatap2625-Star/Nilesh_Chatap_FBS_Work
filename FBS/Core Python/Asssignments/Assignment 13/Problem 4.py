n = int(input("Enter the number of elements in the list: "))

dict = {}

for i in range(1, n + 1):
    dict[i] = i * i

print(dict)