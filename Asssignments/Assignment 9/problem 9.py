def power(m, n):
    if n == 0:
        return 1

    return m * power(m, n - 1)


m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("Answer =", power(m, n))