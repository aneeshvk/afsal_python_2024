x=int(input("Enter first no "))
y=int(input("Enter second no "))
z=int(input("Enter Third no "))
if x<y:
    if x<z:
        print(f"{x} is the smallest")
    else:
        print(f"{z} is the smallest")
else:
    if y<z:
        print(f"{y} is the smallest ")
    else:
        print(f"{z} is the smallest ")



