num=int(input("enter the number"))
l=num//2+1
if num==1:
    print(f"{num} is not prime")
else:
    for i in range(2,l):
        if num%i==0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")