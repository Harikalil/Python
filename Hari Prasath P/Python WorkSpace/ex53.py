def aec(name):
    s=0
    for x in name:
        s+=ord(x)
        
    if s%2==0:
        print("even")
    else:
        print("odd")
    
#calling
name=input("Enter the name :")
aec(name)