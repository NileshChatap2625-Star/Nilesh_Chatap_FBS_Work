n = 6

for i in range(1, 6 + 1):
    print(" " * (6 - i) + "*" + " " * (2 * i - 3) + ("*" if i > 1 else ""))

for i in range(5, 0, -1):
    print(" " * (6 - i) + "*" + " " * (2 * i - 3) + ("*" if i > 1 else ""))