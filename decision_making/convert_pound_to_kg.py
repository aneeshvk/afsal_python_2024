#A pound is equal to 0.4535 kilograms. 
#weight 10
#unit L K
weight =float(input("enter weight>> "))
print("Enter the unit Pound or Kilograms ")
unit=input("Enter P or K >>  ").upper()
if unit =="P":
    converted=weight*0.4535
    print(f"weight is {round(converted,2) } Kilograms ")
elif unit=="K":
    converted=weight/0.4535
    print(f"weight is {round(converted,2)} Pounds ")
else:
     print("Your unit is invalid")
