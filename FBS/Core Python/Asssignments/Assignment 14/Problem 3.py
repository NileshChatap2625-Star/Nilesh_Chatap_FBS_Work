string = ['apple', 'banana', 'cherry', 'date', 'elderberry']

unique_string = set(string)

for item in unique_string:
    count = string.count(item)
    print(item, ":", count)