'''
integer input 
WAPP to accept an integer form the user . 
handle the exception if the user enters a non-numeric value 
'''
try:
    a=int(input("enter integer value = "))
    b=int(input("enter no = "))
    c=a+b
    print(c)
except ValueError as e:
    print(e)
