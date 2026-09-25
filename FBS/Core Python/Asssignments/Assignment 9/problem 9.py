def power(m , n):
    if n == 0:
        return 1
    else:
        return m * power(m, n -1)

m = int(input("enter base:"))
n = int(input("enter power:"))

res = power(m, n)

print("Result = ", res)