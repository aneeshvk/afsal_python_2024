txt=input("Enter any string ")
print(txt)
rev=""
for x in txt:
    #print(x)
    rev=x+rev
    #print(rev)
print(f" reverse string {rev}")