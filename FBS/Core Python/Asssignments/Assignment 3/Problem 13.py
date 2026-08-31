units = float(input("Enter unit of electricity:"))

if(units <= 50):
    bill = units * 0.50
elif(units <= 150):
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif(units <= 250):
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 250) * 1.50)

surcharge = bill * 20/100
total_bill = bill + surcharge

print("Electricity Bill =", bill)
print("Surchargen(20%) =", surcharge)
print("Total Electricity Bill =", total_bill)