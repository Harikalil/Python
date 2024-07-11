#type 4 - No Parameter & with return type 
#function declaration
def primechecker1():
    num=int(input("Enter the Number:"))#9
    c=0
    for x in range(1,num+1):#5
        if num%x==0 :
            c+=1
    if c==2:
        return "prime"
        
    else:
        return "not a prime"
        
