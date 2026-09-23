list =   [10, 20, 30, 40, 50, 60, 70]

sum = 0

## Method 1:  Iterating values


# for ele in list:
#     sum += ele
# print(sum)


### Method 2:  Using indexing

for ind in range(0, len(list)):
    sum += list[ind]

print(sum)