### write a program to calculate profit or loss

cost_price = float(input("Enter the cost price:"))

selling_price = float(input("Enter the selling price:"))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("profit is:", profit)
else:
    loss = selling_price - cost_price
    print("loss is:", loss)