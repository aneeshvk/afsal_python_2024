str1=input("enter any string ")
i=len(str1)-1
rev=""
while i>=0:
    rev=rev+str1[i]
    i=i-1
print(f"Original string = {str1}")
print(f"Reverse string = {rev}")