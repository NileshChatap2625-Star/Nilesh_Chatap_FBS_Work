def prime(n, i):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return prime(n, i + 1)

n = int(input("enteer a number:"))

if prime(n, 2):
    print(n, " is a prime number")
else:
    print(n, "is not a  prime number")