cu={}
def duplicatechecker():
 name=input("enter the name :")
 for x in name:
     if x not in cu:
         cu[x]=1
     else:
         cu[x]+=1
         if cu[x]==2:
             print (x)
    
        
        
#calling
duplicatechecker()
       
 
