total = 0

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    ticket = float(input(f"Enter ticket amount for person {i}: "))

    if age < 12:
        ticket = ticket - (ticket * 0.30)   # 30% discount
    elif age > 59:
        ticket = ticket - (ticket * 0.50)   # 50% discount

    total += ticket

print("Total ticket amount =", total)