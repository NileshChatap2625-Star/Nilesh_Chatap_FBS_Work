n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):

        if i == 1:
            print(j, end=" ")

        elif j == 1:
            print(i, end=" ")

        elif j == n-i+1:
            print(n, end=" ")

        else:
            print(" ", end=" ")

    print()