num1=int(input("Enter the number1 :"))
num2=int(input("Enter the number2 :"))
option=input('''
             Add
             Subract
             Multiply
             Divide
             Type the option you need :  ''')
if option=='Add':
    print("The added number is",num1+num2)
elif option=='Subract':
    print("The Subracted number is",num1-num2)
elif option=='Multiply':
    print("The Multiplied number is",num1*num2)
elif option=='Divide':
    print("The Divided number is",num1/num2)
else :
    print("INVALID OPTION")