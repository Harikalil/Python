'''
Functions - is block statement and which can be reuse 
Function has two parts - Function Declaration & Function Calling 
Function is used to block the complex program into smaller blocks 

Function Types 
1.Built in Function - Math , String , Date 
2.User Defined Function 
    a)Function Declaration 
        i)No Parameter & No return type 
        ii)With Parameter & No return type 
        iii)With Parameter & with return type 
        iv)No Parameter & with Return type 
        
    b)Function Calling 
        i)Call By Value 
        ii)Call By Reference 
'''

#type 1 - No Parameter & No return type 
#function declaration
def primechecker():
    num=int(input("Enter the Number:"))#9
    c=0
    for x in range(1,num+1):#9
        if num%x==0 :
            c+=1
    if c==2:
        print("prime")
    else:
        print("not a prime")
        
#function calling 
primechecker()