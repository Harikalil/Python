#simple if 
#if - else 
# num=int(input("Enter the Number:"))
# if num>0:
#     print("+ive")
# else:
#     print("-ive")
# print("Thank You")

#ladder if 
# num=int(input("Enter the Number:"))
# if num==0:
#     print("Zero")
# elif num<0:
#     print("-ive")
# else:
#     print('+ive')

# nested if 
# num1=int(input("Enter the Number1:"))#8
# num2=int(input("Enter the Number2:"))#5
# num3=int(input("Enter the Number3:"))#16

# if num1>num2:#3>5 8>5
#     if num1>num3:#8>16
#         print("Num 1 is Greater than Num2 & Num3")
#     else:
#         print("Num 3 is Greater than Num1 & Num2")
# else:
#     if num2>num3:#5>6
#          print("Num 2 is Greater than Num1 & Num3")
#     else:
#         print("Num 3 is Greater than Num1 & Num2")

#ternary Operator
# num1=int(input("Enter the Number1:"))
# # print("+ive") if num1>0 else print("-ive")
# print("+ive") if num1>0 else print("-ive") if num1<0 else print ("Zero")


#ladder if 
num1=int(input("Enter the Number1:"))
num2=int(input("Enter the Number2:"))
num3=int(input("Enter the Number3:"))
if num1>num2 and num1>num3:
    print("Num1")
elif num2>num1 and num2>num3:
    print("Num2")
else:
    print("Num3")