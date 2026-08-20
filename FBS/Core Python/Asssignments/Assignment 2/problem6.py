## Take input 

Basic = float(input("Enter Basic Salary: "))

da = float(input("Enter Dearness Allowance (DA): "))
ta = float(input("Enter Travel Allowance (TA): "))
hra = float(input("Enter House Rent Allowance (HRA): "))

## Calculate Gross Salary

Total_salary = Basic + da + ta + hra
print("DA is :", da)
print("TA is :", ta)
print("HRA is :", hra)
print("Gross Salary is :", Total_salary)