a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
d=-b+((b**2)-(4*a*c))/2*a
d1=-b-((b**2)-(4*a*c))/2*a
if d==0:
    print("Both roots are equal")
elif d>0:
    print("Both roots are real and different ")
else:
    print("The roots are imaginary and no solution ")