def fibonnacy(num):
    a = 0
    b = 1
    for i in range(1, num + 1):
        print(a, end=' ')
        c = a + b
        a = b
        b = c 

num = int(input("Enter a number:"))
res = fibonnacy(num)
print(res)