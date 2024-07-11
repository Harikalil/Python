#type 2 - With Parameter & No return type 
#function declaration
def primechecker(num):
    c=0
    for x in range(1,num+1):#5
        if num%x==0 :
            c+=1
    if c==2:
        print("prime")
    else:
        print("not a prime")
        
#function calling 
Num1=int(input("Enter the Number1:"))#1
Num2=int(input("Enter the Number2:"))#4
a=Num1+Num2
primechecker(a)