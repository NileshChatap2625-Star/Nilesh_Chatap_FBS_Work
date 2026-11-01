dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

count = 0

for value in dict.values():
    count = count + value

print("Sum of all values in the dictionary:", count)