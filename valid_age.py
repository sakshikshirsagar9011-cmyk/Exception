'''
age validation
'''
try:
    age=int(input("enter age = "))
    print(age)
except Exception as e:
    print("invalid integers ",e)    