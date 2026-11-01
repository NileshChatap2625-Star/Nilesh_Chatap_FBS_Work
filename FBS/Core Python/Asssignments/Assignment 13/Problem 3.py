dict = {'name': 'nilesh', 'age': 20, 'course': 'python'}

key = input("Enter the key to check: ")

if key in dict:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")