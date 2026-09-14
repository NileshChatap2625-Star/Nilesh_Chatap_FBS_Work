price1 = int(input("Enter price of first item:"))
price2 = int(input("Enter price of second item:"))
price3 = int(input("Enter price of third item:"))
price4 = int(input("Enter price of fourth item:"))
price5 = int(input("Enter price of fifth item:"))

total_price = price1 + price2 + price3 + price4 + price5

gst = total_price * 0.18

final_price = total_price + gst

print("Total price of items =", total_price)
print("GST amount =", gst)
print("Final price after adding GST =", final_price)