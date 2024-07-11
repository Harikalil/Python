start=int(input("Enter starting number : ")) 
stop=int(input("Enter ending number : ")) 

for x in range(start,stop+1):
    s=1
    for y in range(2,x+1):
        if x%y==0:
            s+=1
    if s==2:
        print(x)
        
    
    
