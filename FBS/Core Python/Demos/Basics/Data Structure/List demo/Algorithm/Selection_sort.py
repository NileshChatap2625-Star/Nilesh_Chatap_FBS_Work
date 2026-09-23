# def selectionsort(list):
#     size = len(list)
#     for i in range(0, size - 1):
#         min_ind = i
#         for j in range(i+1, size):
#             if(list[j] < list[min_ind]):
#                 min_ind = j
#         list[i], list[min_ind] = list[min_ind], list[i]

# list = [50, 40, 30, 20, 10]
# print(list)
# selectionsort(list)
# print(list)


def selection(list):
    size = len(list)
    for i in range(0, size-1):
        min = i
        for j in range(i+1, size):
            if(list[j] < list[min]):
                min = j
            list[i], list[min] = list[min], list[i]

list = [50, 40, 30, 20, 10]
print(list)
selection(list)
print(list)