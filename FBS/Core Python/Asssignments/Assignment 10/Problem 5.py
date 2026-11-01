list = [10, 20, 30, 50, 40, 10, 30]

num = int(input("Enter a number:"))

count = 0

for i in list:
    if i == num:
        count = count + 1

if count > 0:
    print("Element is prasent")
    print(f'Element are prassent {count}, times')
else:
    print("Element is not present")