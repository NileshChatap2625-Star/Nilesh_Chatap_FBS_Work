## 5. Write a program to check whether the triangle is equilateral, isosceles or scalene
#     triangle.

a = int(input("Enter first side of triangle: "))
b = int(input("Enter second side of triangle: "))
c = int(input("Enter third side of triangle: "))

if a == b and b == c:
    print("Triangle is Equilateral.")
elif a == b or b == c or a == c:
    print("Triangle is Isosceles.")
else:
    print("Triangle is Scalene.")