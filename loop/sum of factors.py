n=int(input("enter the number <<"))
print(f"Factors of {n} are ")
for i in range(1,n+1):
    if n%i==0:
        s=s+i
print(i)


