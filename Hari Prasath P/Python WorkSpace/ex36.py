maths=int(input("Enter your maths mark : "))
phy=int(input("Enter your physics mark : "))
chem=int(input("Enter your chemistry mark : "))
total=maths+phy+chem
tot=maths+phy
if maths>=65 and phy>=55 and chem>=50 and total>=190 and tot>=140:
    print("The candidate is elegible")
else :
    print("The candidate is not elegible")