def aec():
    s=0
    name=input("Enter your name :")
    for x in name:
        s+=ord(x)
        
    if s%2==0:
        print("even")
    else:
        print("odd")
    
#calling
aec()