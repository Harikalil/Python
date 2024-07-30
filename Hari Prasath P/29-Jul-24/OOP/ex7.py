number=input("Enter the number :")#12345
k=''
for x in number :
    if int(x)%2==0:
        k=k+'0'
    else:
        k=k+'1'
print(k)     
        