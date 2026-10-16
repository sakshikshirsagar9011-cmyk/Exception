'''
multiple exception 
'''
try:
    a=int(input("enter no = "))
    b=int(input("enter 2 no = "))
    c=a//b
    print(c)
except Exception as e:
    print(e)    