bp=int(input("Enter the number persons big bet :"))
abig=int(input("Enter the amount of bets in big :"))
sp=int(input("Enter the number persons small bet :"))
asmall=int(input("Enter the amount of bets in small :"))
big=bp*abig
small=sp*asmall
if big > small:
    print ("SMALL")
else:
    print ("BIG")
    