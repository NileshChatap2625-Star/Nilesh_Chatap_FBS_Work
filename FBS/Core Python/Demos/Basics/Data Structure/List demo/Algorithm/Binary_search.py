#####  Searching element by using binary search

def binarysearch(list, search_ele):
    beg = 0
    end = len(list) - 1
    

    while(beg <= end):
       mid = (beg + end) // 2
       if(search_ele == list[mid]):
           return mid
       elif(search_ele < list[mid]):
           end = mid - 1
       elif(search_ele > list[mid]):
          beg = mid + 1
    else:
       return -1

    

list = [10, 20, 30, 40, 50, 60]
ele = 50
res = binarysearch(list, ele)
if(res != -1):
    print(f'{ele} is prasent at index {res}')
else:
    print(f'{ele} is not prasent in list')