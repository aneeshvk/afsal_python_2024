n=int(input("enter the number)"))
sum_digits=0
num=n
count = 0
while num != 0:
    #print(f"Number of digits {num}")
    num //= 10
    count += 1
num=n
while num != 0:
     t=num%10
     sum_digits=sum_digits+t**count
     num //= 10
if n==sum_digits:
     print(f"{n} is armstrong")
else:
     print(f"{n} is not armstrong")