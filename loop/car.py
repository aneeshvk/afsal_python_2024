import sys
print("1. Start\n2. Stop \n3. Quit \n Enter ur choice  ")
carStatus=False
while True:
    op=int(input(">> "))
    if op==1:
        if carStatus:
            print("Car already Started...")
        else:
            print("Car started...")
            carStatus=True
    elif op==2:
        if carStatus:
            print("Car Stoped...")
            carStatus=False
        else:
            print("Car Alreay Stoped...")
    elif op==3:
        sys.exit(0)
    else:
        print("invalid choice")