## Take inpute of hours, minutes and seconds

Hours = int(input("enter hours:"))
Minutes = int(input("enter minutes:"))
Seconds = int(input("enter seconds:"))

## Calculate total seconds

Total_seconds = (Hours * 3600) + (Minutes * 60) + Seconds
print("Total seconds:", Total_seconds)