import random
while True:
    hiddenValue=random.randint(1,9)
    i=1
    pointsGet=20
    print("Enter ur guess u have three chances..")
    while i<=3:
        yourGuess=int(input(">> "))
        if yourGuess==hiddenValue:
            print("you won!!....")
            print(f"You got {pointsGet} points")
            break
        pointsGet-=i*5
        i+=1
    else:
        print("you lost!!....")
        print(hiddenValue)
    print("Do u want to go another turn..continue press y/Y")
    choice=input(">> ").upper()
    if choice!="Y":
        break

