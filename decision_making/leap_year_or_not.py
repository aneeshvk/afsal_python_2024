#leap year or not
# y %4==0 
year=int(input("enter the year:"))
if year % 4==0:
    if year %100==0:
        if year%400==0:
            print(f"the {year} is leap")
        else:
            print(f"{year} is not leap year")
    else:
        print(f"the {year} is leap")
else:
    print(f"{year} is not leap year")

