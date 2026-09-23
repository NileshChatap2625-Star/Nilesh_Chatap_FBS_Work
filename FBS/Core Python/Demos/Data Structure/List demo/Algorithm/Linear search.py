def linearSearch(list, search_ele):
    size = len(list)
    for ind in range(0, size):
        if(list[ind] == search_ele):
            return ind
    else:
        return -1

list = [10, 50, 90, 30, 80, 40]
ele = 40
res = linearSearch(list, ele)
if(res != -1):
    print(f'{ele} is prasent at index {res}')
else:
    print(f'{ele} is not prasent in list')  