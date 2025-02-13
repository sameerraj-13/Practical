# Python CODE for the practical. #

# CODE 1:

#To find the max no among the three no.

def max_no(a,b,c):
    return max(a,b,c)
     

a = int(input("Enter the 1st no:"))
b = int(input("Enter the 2nd no:"))
c = int(input("Enter the 3rd no:"))

no = max_no(a,b,c)
print("The max no is:", no)

# CODE 2:

#To print the table of the given no.
def table(n):
    for i in range (1,11):
        print (n, "x", i, "=", n*i)
        
n = int(input("Enter the no:"))
print("Table of", n, "is:")
table(n)

# CODE 3:

def tri(n):
    count = 1
    for i in range (1,n):
        for j in range (1,i+1):
            print(count, end=" ")
            count += 1
        print()
n = int(input("Enter the no:"))
tri(n)

# CODE 4:

def invert(n):
    for i in range (1, n):
        for j in range (1, i+1):
            print (i, end=" ")
        print()
n = int(input("Enter the no:"))
invert(n)

# CODE 5:

# To print the triangle of stars. Sidha triangle.
def tri(n):
    for i in range (1,n):
        for j in range (1,n-i):
            print(" ", end=" ")
        for k in range (2*i-1):
            print("*", end=" ")
        print()
n = int(input("Enter the no:"))
tri(n)

# CODE 6:

# To print the triangle of stars. Ulti triangle.
def tri(n):
    for i in range (1,n):
        for j in range (1,i+1):
            print(" ", end=" ")
        for k in range (2*(n-i)-1):
            print("*", end=" ")
        print()
n = int(input("Enter the no:"))
tri(n)
