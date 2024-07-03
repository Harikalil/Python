cm=float(input("enter the value:"))
option=input('meter\nkilometer\nenter your option:')
if option=='meter':
    m=cm/100
    print("the converted value is:",m)
elif option=='kilometer':
    km=cm/100000
    print("the converted value is:",km)