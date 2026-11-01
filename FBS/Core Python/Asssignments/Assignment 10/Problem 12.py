list = [1, 2, 3, 4, 5]

square = []
cube = []

for i in list:
    square.append(i * i)
    cube.append(i * i * i)

print("Orignal list=", list)
print("square list=", square)
print("cube list=", cube)