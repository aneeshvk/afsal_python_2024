print("Enter a Number ")
n=int(input("> "))
print(f"Factors of {n} are ")
for i in range(1,n+1):
    if n%i==0:
        print(i)