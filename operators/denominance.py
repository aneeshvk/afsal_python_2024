#program to convert currency
totalAmount=int(input("enter your total amount"))
five_hrds =totalAmount//500
totalAmount%=500 # totalAmount=totalAmount%500
two_hrds=totalAmount//200
totalAmount%=200
hrds=totalAmount//100
totalAmount%=100
fifty=totalAmount//50
totalAmount%=50
twenty=totalAmount//20
totalAmount%=20
ten=totalAmount//10
totalAmount%=10
print("Available Denominations ")
print(f" 500 : {five_hrds} \n 200 : {two_hrds}\n 100 : {hrds}")
print(f" 50 : {fifty} \n 20 : {twenty}\n 10 : {ten}\n Coins : {totalAmount}")
