## take input of price and discount

cp = float(input("Enter cost price:"))
discount = float(input("Enter discount:"))

## calculate selling price

discount_amount = (discount / 100) * cp
sp = cp - discount_amount
print("Selling price:", sp)
