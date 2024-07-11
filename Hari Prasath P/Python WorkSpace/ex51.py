def fact():
    num=int(input("enter a number :"))
    factorial=1
    if num < 0:
        return "the factorial not for 0"
    else:
        for x in range(num, 0,-1):
            factorial *= x
        return f"The factorial of {num} - {factorial}"



#calling


print(fact())