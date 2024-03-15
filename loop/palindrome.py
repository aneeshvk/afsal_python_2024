num=int(input("enter the number"))
num=str(num)
print(f"Your Number {num}")
print(f"reverse of number {num[::-1]}")
if num == num[::-1]:
    print(" its a palindrome")
else:
    print(" its not a palindrome")
# num2=num
# reversed_num=0
# while num != 0:
#      t=num%10
#      digit = num % 10
#      reversed_num = reversed_num * 10 + digit
#      num //= 10
# if num2 == reversed_num:
#     print(" its a palindrome")
# else:
#     print(" its not a palindrome")

