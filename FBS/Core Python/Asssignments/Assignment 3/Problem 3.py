#### 3. Write a program to input angles of a triangle and check whether triangle is valid 
#       or not.

angle1 = int(input("Enter first angle of triangle: "))
angle2 = int(input("Enter second angle of triangle: "))
angle3 = int(input("Enter third angle of triangle: "))

if angle1 + angle2 + angle3 == 180:
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")