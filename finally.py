'''
using finally 
'''
try:
    a=int(input("enter integer value = "))
    b=int(input("enter no = "))
    c=a+b
    print(c)
except ValueError as e:
    print(e)
finally:
    print("program exicution is complited")    