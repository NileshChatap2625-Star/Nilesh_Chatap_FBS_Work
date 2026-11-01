list = [10, 50, 40, 90, 80, 60, 100]

max1 = list[0]
max2 = list[0]

for ind in range(0, len(list)):
    if(list[ind] > max1):
        max2 = max1
        max1 = list[ind]
    elif(list[ind] > max2):
        max2 = list[ind]

print('Maximum number =', max1)
print('2nd Maximum number =', max2)