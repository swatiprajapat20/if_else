
month=input("enter the month:")
if month=="feb":
    print("no. of days 28 or 29")
elif month in("jan,march,may,july,aug,oct,dec"):
    print("no. of days 31 days")
elif month in ("april,june,september,november"):
    print("No. of days:30")
else:
    print("no. of days 30 days")



