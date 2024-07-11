num=int(input("enter the number:"))
sum=0
Temp=num
while Temp > 0:
    Factorial = 1
    Reminder = Temp % 10
    for x in range(Reminder, 0,-1):
        Factorial *= x
    sum+=Factorial
    Temp //=10
if sum == num:
      print(f"{num} is a strong number.")
else:
      print(f"{num} is not a strong number.")