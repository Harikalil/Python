cu={}
def duplicateremover():
    name=input("enter the name:")
    for x in name:
        if x not in cu:
            cu[x]=1
        else:
            cu[x]+=1
    print(cu)    
        
        
#calling
duplicateremover()
    
    