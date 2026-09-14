## syntax:
# map(function, iterbles)


# Method 1:

# def square(n):
#     return n * n

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = list(map(square, data))

# print(res)


## Methode 2:


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = list(map(lambda n: n * n, data))

print(res)