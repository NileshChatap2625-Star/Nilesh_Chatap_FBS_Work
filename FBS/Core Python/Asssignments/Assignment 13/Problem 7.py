dict = {'name': 'nilesh', 'age': 20, 'course': 'python'}

key = input("enter the key to remove: ")

if key in dict:
    del dict[key]
    print("Key removed from the dictionary.")
    print(dict)
else:
    print("Key does not exist in the dictionary.")