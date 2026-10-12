

for i in range(1,12):
    for j in range(1,12):
        if i == 1 or i == 11 or i + j == 11:
            print("*", end="")
        else:
            print(" ", end="")
    print()


