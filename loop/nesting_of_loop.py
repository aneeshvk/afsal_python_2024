#https://www.upgrad.com/blog/python-pattern-programs/
#https://pynative.com/print-pattern-python-examples/
# for i in range(1,6):
#     for i in range(1,6):
#         print()
"""
 *  
 *   *
 *   *   *
 *   *   *   *
 *   *   *   *   *
"""
# for i in range(1,6):    
#     for j in range(1, i + 1):  
#         print(" * ", end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{j}", end="")
#     print()    

# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i}",end="")
#     print()    

# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i*j}",end="")
#     print() 

# for i in range(1,6):
#     for j in range(1,6):
#         print(i+1,end="") 
#     print()  

"""
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f"{j} ", end="")
#     print()   

"""
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f"{i} ", end="")
#     print()  

"""
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

# k=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(f"{k} ", end="")
#         k=k+1
#     print() 

"""
5 5 5 5 5 
4 4 4 4
3 3 3
2 2
1
"""

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(f"{i} ",end="")
#     print()
"""
1 1 1 1 1 
2 2 2 2
3 3 3
4 4
5
"""

# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(f"{i} ",end="")
#     print()

"""
1 
2 1       
3 2 1     
4 3 2 1   
5 4 3 2 1 
"""

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(f"{j} ",end="")
#     print()    
    


for i in range(1,6):
    for j in range(1,i+1):
        print(f"{j} ", end="")
    print()   
