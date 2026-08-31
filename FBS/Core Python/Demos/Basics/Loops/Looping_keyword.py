
### 1. pass :  -----> neglect expected indentation error

for i in range(1, 10):
    pass



### 2. break :   ----> for terminating the loop

for i in range(1, 10):
    if (i == 4):
        break
    print(i)


### 3. continue :  ------> to stop perticular interation

for i in range(1, 10):
    if (i == 4):
        continue
    print(i)


### 4. else :       ---------> will exicute when the loop is exicute successfully

for i in range(1, 10):
    if (i == 4):
        continue
else:
    print("Else block exicuted")