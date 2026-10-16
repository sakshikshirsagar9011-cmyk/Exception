'''
Division of two number 
write a python program to divide two number handle the exception that occure when the denominator is zero 
'''
try:
    no1=int(input("enter frist no ="))
    no2=int(input("enter second no = "))
    c=no1//no2
    print(c)

except ZeroDivisionError as e :
    print("no con not be ",e)