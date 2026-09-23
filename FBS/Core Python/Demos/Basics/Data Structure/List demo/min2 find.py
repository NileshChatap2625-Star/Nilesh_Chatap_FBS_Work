#### minimum and 2nd mini number find


list = [40, 50, 10, 70, 20, 90, 100]

min = list[0]
min2 = list[0]
for ind in range(0, len(list)):
    if(min > list[ind]):
        min2 = min
        min = list[ind]
    elif(min2 > list[ind]):
        min2 = list[ind]

print('Min number : ', min)
print('min2 number : ', min2)






