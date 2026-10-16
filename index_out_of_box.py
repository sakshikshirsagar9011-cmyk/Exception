'''
list index error 
'''
try:
    list1=[10,20,30,40,50]
    serch1=int(input("enter no = "))
    for i in range(len(list1)):
        if serch1==i:
            print(list1[i])
            break
    else:
        print(" index not found")        
        

except IndexError as e:
    print(e)    