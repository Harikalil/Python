def calculating(i):
    num1=int(input(f"enter the internal value student {i+1}:"))
    num2=int(input(f"enter the external value student {i+1}:"))
    total=num1+num2 
    s=(total/100)*60
    return s

no=int(input("Enter the number of student:"))
mark=[]
for x in range(no):
    
    mark.append(calculating(x))


print(mark)