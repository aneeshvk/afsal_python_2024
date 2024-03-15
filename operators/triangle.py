#to find area of a triangle
import math
a=float(input("enter the first side "))
b=float(input("enter the second side "))
c=float(input("enter the third side "))
#to find the semi perimeter
s=(a + b + c)/2
#find area of the triangle
m=(s*(s-a)*(s-b)*(s-c))**0.5
#area =math.sqrt(m)
print("the area of the triangle ",m)
