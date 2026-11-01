list = [10, 15, 13, 7, 20, 23, 18]

even = []
odd = []

for num in list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Original list:", list)
print("Even numbers:", even)
print("Odd numbers:", odd)