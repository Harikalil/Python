unit=int(input("Enter electric the unit used :"))
if unit<=50:
    print("The Bill amount is : ",0.50*unit+unit*20/100)
elif unit>50 and unit<=150:
    print("The Bill amount is : ",0.75*unit+unit*20/100)
elif unit>150 and unit<=250:
    print("The Bill amount is : ",1.20*unit+unit*20/100)
elif unit>250:
    print("The Bill amount is : ",1.50*unit+unit*20/100)
    