## 1. To pass multiple para to function
## 2. mention asterisk(*) symbol before parameter in function defination
## 3. Value will be store in tuple formate
## 4. Use for loop to iterate value from tuple



def addition(*num):
    sum = 0
    for i in num:
        sum += i
    return sum

res = addition(10, 20, 30, 40, 50)
print(res)