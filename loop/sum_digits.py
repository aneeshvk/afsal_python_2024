num=int(input("enter the number"))
sum_digits=0
while num != 0:
     t=num%10
     sum_digits=sum_digits+t
     num //= 10
print(f"sum of digits {sum_digits}")


        