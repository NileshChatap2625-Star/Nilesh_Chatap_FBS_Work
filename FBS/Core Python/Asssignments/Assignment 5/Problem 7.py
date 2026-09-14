###1.  Factorial 

n = int(input("Enter number:"))

fact = 1
sum = 0

for i in range(1, n+1):
    fact = fact * i
    sum = sum + fact 

print("sum of number=", sum)



### 2. square root

n = int(input("Enter number:"))

sum = 0

for i in range(1, n+1):
    sum = sum + n ** i
print("sum=", sum)


### 3. geometric series from 1 to n common ratio = 2

n = int(input("Enter number:"))

term = 1
sum = 0

for i in range(1, n+1):
    sum = sum + term
    term = term * 2
    
print("sum=", sum)



#### 4. 


n = int(input("Enter number:"))

sum = 0
for i in range(1, 11):
    sum = sum + (n ** i) / i

print("sum=", sum)



##### 5. 

x = int(input("Enter number:"))
n = int(input("Enter number:"))
sum = 0
sign = 1

for i in range(1, n+1):
    denominator = 2 * i - 1
    term = (x ** denominator) / denominator
    sum = sum + sign * term
    sign = sign * -1

print("sum=", sum)