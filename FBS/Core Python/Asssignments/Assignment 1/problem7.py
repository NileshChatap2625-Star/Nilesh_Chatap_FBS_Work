## Take input 

a = float(input("Enter a :"))
b = float(input("Enter b :"))
c = float(input("Enter c :"))

## Calculate discriminant

d = (b*b) - (4*a*c)

# calculate roots

if d > 0:
    root1 = (-b + d**0.50) / (2*a)
    root2 = (-b - d**0.50) / (2*a)
    print("The roots are real and different.")
    print("Root 1 is :", root1)
    print("Root 2 is :", root2)
elif d == 0:
    root = -b / (2*a)
    print("The roots are real and equal.")
    print("Root is :", root)
else:
    print("The roots are complex.")
