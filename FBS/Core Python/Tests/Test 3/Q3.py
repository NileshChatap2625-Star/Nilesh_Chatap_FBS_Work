n = int(input("enter number of emp:"))

total_salary = 0

for i in range(1, n+1):
    basic = float(input("enter basic salary:"))

    if(basic < 20000):
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    salary = basic + da + ta + hra

    print("emp", i, "=", salary)

    total_salary = total_salary + salary

    print("total salary=", total_salary)
