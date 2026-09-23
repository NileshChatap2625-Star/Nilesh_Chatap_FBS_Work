def bubblesort(list):
    size = len(list)
    for i in range(1, size):
        for j in range(0, size - 1):
            if(list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
                print(list)

list = [50, 40, 30, 20, 10]
print(list)
bubblesort(list)
print(list)