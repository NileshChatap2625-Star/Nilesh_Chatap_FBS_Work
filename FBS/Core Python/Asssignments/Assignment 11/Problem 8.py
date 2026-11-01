number = list(range(1, 101))

for row in range(10):
    start = row * 10
    end = start + 10

    current_row = number[start:end]

    if row % 2 == 0:
        current_row.sort()

    for num in current_row:
        print(num, end="  \t")

    print()