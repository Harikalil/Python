def factorial(a):
    factorial=1
    if a < 0:
        return "the factorial not for 0"
    else:
        for x in range(a, 0,-1):
            factorial *= x
        return f"The factorial of {a} - {factorial}"


a=int(input("Enter the number : "))
print(factorial(a))