## Take input of distance infeet and inches

feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

## calculate total inches

Total_inches = (feet * 12) + inches

## Calculate meters and centimeters

meters = Total_inches * 0.0254
centimeters = Total_inches * 2.54

print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)