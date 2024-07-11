#type 3 - With Parameter & with return type 
#function declaration
def primechecker(num):
    c=0
    for x in range(1,num+1):#5
        if num%x==0 :
            c+=1
    if c==2:
        return "prime"
        
    else:
        return "not a prime"
        
