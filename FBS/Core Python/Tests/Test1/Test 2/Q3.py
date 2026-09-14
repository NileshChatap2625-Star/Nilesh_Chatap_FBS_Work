import math

length = 50
breadth = 40
radius = 20
cost_per_meter = 35
times = 5


semicircle = math.pi * radius

perimeter = (2 * length) + breadth + semicircle

total_wire = perimeter * times

total_cost = total_wire * cost_per_meter

print("perimeter of field =", perimeter)
print("total wire required =", total_wire)
print("total cost of wire =", total_cost)