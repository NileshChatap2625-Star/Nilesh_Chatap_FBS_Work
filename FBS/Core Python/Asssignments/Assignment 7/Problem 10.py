n = 5

for i in range(1, n + 1):
    # Left numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")

    # Right numbers
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()


