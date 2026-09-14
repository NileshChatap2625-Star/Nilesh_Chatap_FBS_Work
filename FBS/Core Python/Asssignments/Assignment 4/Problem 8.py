start = int(input("Enter a number:"))
end = int(input("Enter a number:"))

for i in range(start, end + 1):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)