area = float(input("Enter area of one wall: "))
interior_cost = float(input("Enter interior painting cost per sq.ft: "))
exterior_cost = float(input("Enter exterior painting cost per sq.ft: "))

interior = area * interior_cost
exterior = area * exterior_cost

total = interior + exterior

print("Interior painting cost =", interior)
print("Exterior painting cost =", exterior)
print("Total painting cost =", total)