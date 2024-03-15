name=input("enter any string ")
i=len(name)-1
rev=""
while i>=0:
    rev=rev+name[i]
    i=i-1

print(f"original name={name}")
print(f"reverse string={rev}")

if name==rev:
    print("Is a palindrome")
else:
    print("Is not a palindrome")

