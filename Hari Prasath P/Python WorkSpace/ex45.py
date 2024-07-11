num1=int(input("starting : "))
num2=int(input("ending : "))
m=int(input("The number to be multiplied : "))
for x in range (num1,num2+1,1):
    print(f'{m}x{x}={m*x}')
