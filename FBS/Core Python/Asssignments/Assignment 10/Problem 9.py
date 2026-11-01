list = [10, 12, 7, 5, 40, 15, 3]

even = []
odd = []

for i in list:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print("Even list=", even)
print("Odd list= ", odd)
