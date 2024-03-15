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
match op:
    case "1":
        print(f"{x} + {y} = {x+y}")
    case "2":
        print(f"{x} - {y} = {x-y}")
    case "3":
        print(f" {x} * {y} = {x*y}")
    case "4":
        print(f"{x} / {y} = {x/y}")
    case "5":
        print(f" {x} ** {y} = {x**y}")
    case "6":
        print(f" {x} % {y} = {x%y}")
    case "7":
        print(f" {x} // {y} = {x//y}")  
    case _:
        print("Invalid Operation ") 

      