dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

product = 1

for value in dict.values():
    product = product * value

print("Product of all values in the dictionary:", product)