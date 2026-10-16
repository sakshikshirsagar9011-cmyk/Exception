'''
password length check 
'''
try:
    password=input("enter password = ")
    if len(password)<6 :
        raise ValueError("plz enter atlist 6 characters ")
    print(password)

except Exception as e:
    print(e)        
