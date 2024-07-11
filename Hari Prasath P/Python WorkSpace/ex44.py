start=int(input("Enter the starting number :"))
stop=int(input("Enter the ending number :"))
s=int(input("Enter the number : "))
for x in range (start,stop,1):
    print(f'{x}x{s}={x*s}')