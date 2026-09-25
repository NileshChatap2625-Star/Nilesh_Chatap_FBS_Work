def digit_count(n):
    temp = n
    count = 0
    while temp > 0:
        count += 1
        temp = temp // 10
    return count

def armstrong_sum(n, count):
    if n == 0:
        return 0
    else:
        d = n % 10
        return (d ** count) + armstrong_sum(n // 10, count)


n = int(input("enter number:"))
count = digit_count(n)
result = armstrong_sum(n, count)

if result == n:
    print(f'{n} is an armstrong number.')
else:
    print(f'{n} is not an armstrong number.')