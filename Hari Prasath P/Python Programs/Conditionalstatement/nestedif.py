num1=int(input("Enter the number1"))
num2=int(input("Enter the number2"))
num3=int(input("Enter the number3"))
if num1>num3:
    if num1>num2:
        print("Num1 is greater")
    else:
        print("Num2 is greater")
else:
    if num2>num3:
        print("Num2 is greater")
    else:
        print("Num3 is greater")