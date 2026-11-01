list = [10, 20, 40, 30, 90, 70, 50]

max = list[0]
min = list[0]

for ind in range(0, len(list)):
    if(list[ind] > max):
        max = list[ind]
    if(min > list[ind]):
        min = list[ind]

print("Maximum number=", max)
print('Minimum number=', min)