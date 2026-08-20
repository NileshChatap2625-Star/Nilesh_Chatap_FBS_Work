num = 578

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

print(f"d1:{d1}, d2:{d2}, d3:{d3}.")
print(num)