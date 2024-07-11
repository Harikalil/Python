def fact(num):
    factorial=1
    if num < 0:
        print("the factorial not for 0")
    else:
        for x in range(num, 0,-1):
            factorial *= x
        print(f"The factorial of {num} - {factorial}")

        
        
        
#calling 
num=int(input("enter a number :"))
fact(num)