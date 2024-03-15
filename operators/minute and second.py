#program to convert seconds
second=int(input("Enter the time i seconds "))
second=second % (24 * 3600)
h=second // 3600
second =second % 3600
m=second // 60
second = second %60
print(f"H :{h} , M: {m}, S:{second}")
