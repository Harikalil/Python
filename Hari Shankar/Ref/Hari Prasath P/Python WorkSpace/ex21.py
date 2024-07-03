basic=int(input("Enter your basic salary :"))
if basic<=10000 :
    print("The HRA = ",basic*20/100,"The DA = ",basic*80/100)
elif basic<=20000:
    print("The HRA = ",basic*25/100,"The DA = ",basic*90/100)
elif basic>20000:
    print("The HRA = ",basic*30/100,"The DA = ",basic*95/100)
     