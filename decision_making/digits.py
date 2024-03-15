n=int(input("enter a number: "))
# if n>=0 and n<=9:
#     print("is a one digit no")
# elif n>=10 and n<=99:
#     print("is a two digit no")
# elif n>=100 and n<=999:
#     print("is a three digit no")
# else:
#     print("is more than three digit no")

if 0<=n<=10:
     print("is a one digit no")
elif 10<=n<=99:
    print("is a two digit no")
elif 100<=n<=999:
    print("is a three digit no")
else:
    print("is more than three digit no")