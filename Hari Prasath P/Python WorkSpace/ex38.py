rno=int(input("Enter the student roll number :"))
name=input("Enter the student name : ")
phy=int(input("Enter the mark scored in physics :"))
chem=int(input("Enter the mark scored in chemistry : "))
ca=int(input("Enter the mark scored in computer application :"))
total=phy+chem+ca
percentage=(total/300)*100
print(f"The roll number of the student : {rno}\n The name of the student : {name} \n The mark scored in physics : {phy} \nThe mark scored in chemistry : {chem} \nThe mark scored in computer application : {ca} \n The total marks : {total} \n The percentage scored : {percentage}")
