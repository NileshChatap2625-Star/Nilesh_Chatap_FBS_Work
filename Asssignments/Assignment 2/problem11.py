amount = int(input("Enter amount:"))

n2000 = amount // 2000
amount = amount % 2000

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

print("Number of 2000 notes:", n2000)
print("Number of 500 notes:", n500)
print("Number of 200 notes:", n200)
print("Number of 100 notes:", n100)
print("Number of 50 notes:", n50)
print("Number of 20 notes:", n20)
print("Number of 10 notes:", n10)

total_notes = n2000 + n500 + n200 + n100 + n50 + n20 + n10
print("Total number of notes:", total_notes)