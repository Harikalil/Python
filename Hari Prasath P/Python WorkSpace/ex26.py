num1=int(input("Enter a positive number 1 :"))
num2=int(input("Enter a positive number 2 :"))
if num1>0 and num2>0 :
    num3=num1+num2
    print("The added value of the two positive number is :",num3)
    if num3%2==0 :
        print("The added value is Even")
    if num3%2==1 :
        print("The added value is odd")
else :
    print ("Entered a Negative number")