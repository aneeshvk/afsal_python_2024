n=int(input("enter the number"))
sum=0
l=n//2+1
for i in range (1,l):
     if(n%i==0):
         sum =sum +i
if(sum==n):
    print(f"{n} is perfect number") 
else:
    print(f"{n} is not perfect number")   