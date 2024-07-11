def aec(name):
    s=0
    for x in name:
        s+=ord(x)
        
    if s%2==0:
        return "even"
    else:
        return "odd"
    
#calling
name=input("Enter the name :")
print(aec(name))