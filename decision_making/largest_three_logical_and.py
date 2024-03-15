x=int(input("Enter first no "))
y=int(input("Enter second no "))
z=int(input("Enter Third no "))

if x>y and x>z:
    print(f"{x} is the largest")
elif y>z:
    print(f"{y} is the largest")
else:
    print(f"{z} is the largest")