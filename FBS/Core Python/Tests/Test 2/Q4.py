length = int(input("Enter length of wall:"))
height = int(input("Enter height of wall:"))
rate = int(input("Enter painting cost per square meter:"))

area = 4 * length * height
total_cost = area * rate

print("Area of wall =", area)
print("Total cost of painting =", total_cost)
