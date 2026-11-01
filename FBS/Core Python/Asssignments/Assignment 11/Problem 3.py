list = [[1, 5], [2, 2], [3, 8], [4, 1]]

list.sort(key=lambda x: x[1])

print("List sorted by second element of each sublist:", list)