
num=int(input("enter the number"))
count = 0
sum_digits=0
while num != 0:
    #print(f"Number of digits {num}")
    num //= 10
    count += 1

print(f"Number of digits {count}")

#print(f"Number of digits {len(str(num))}")