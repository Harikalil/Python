num=int(input("enter the number:"))
factorial=1
if num < 0:
    print("the factorial not for 0")
else:
    for x in range(num, 0,-1):
        factorial *= x
print(f"The factorial of {factorial}")
