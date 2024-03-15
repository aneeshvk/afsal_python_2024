#calculate compound interset
p=float(input("enter the principal amount"))
n=int(input("enter the time period")) 
r=float(input("enter the rate of interest"))
a=p *(1+r/100)**n
i=a-p
print('Total Amount ',a)
print('Interest ',i)