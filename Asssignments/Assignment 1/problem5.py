## Take input

a = int(input("Enter principal amount: "))
b = int(input("Enter rate of interest: "))
c = int(input("Enter time period: "))

## Perform calculation

compound_interest = a * (1 + b / 100) ** c
print("Compound Interest :", compound_interest)