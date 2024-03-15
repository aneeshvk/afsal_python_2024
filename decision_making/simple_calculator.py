# x,y Two nos as inputs
# operation 1. addition 2. substraction 3. Multiplication 4. Division 5 Exponentiation 6 Modular division

print("""
1. addition
2. substraction
3. Multiplication
4. Division
5. Exponentiation
6. Modulus
7. Floor division
""")
op=input("Select Operation>>  ").upper()
x=int(input("enter the first number "))
y=int(input("enter the second number "))
if op=="1":
    print(f"{x} + {y} = {x+y}")
elif op=="2":
    print(f"{x} - {y} = {x-y}")
elif op=="3":
    print(f" {x} * {y} = {x*y}")
elif op=="4":
    print(f"{x} / {y} = {x/y}")
elif op=="5":
    print(f" {x} ** {y} = {x**y}")
elif op=="6":
    print(f" {x} % {y} = {x%y}")
elif op=="7":
    print(f" {x} // {y} = {x//y}")   
else:
    print("Invalid Operation ") 

      