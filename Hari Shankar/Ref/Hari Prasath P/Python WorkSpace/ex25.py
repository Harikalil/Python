post=input("Enter your position in the office :")
exp=int(input("Enter your experience in the office :"))
salary=int(input("Enter your salary :"))
if exp>0:
    print(post,"with the experience of ",exp,"Years","Oh great! The increament of the month for you is:",salary*exp/100,"The total new salary is :",salary+salary*exp/100)
    