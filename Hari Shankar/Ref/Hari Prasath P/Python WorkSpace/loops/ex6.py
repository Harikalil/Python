start=int(input("enter the starting number:"))
stop=int(input("enter the ending number:"))
n1="HariprasathP"
n2="Harishankar"
c1=len(n1)
c2=len(n2)
for x in range (start,stop+1,1):
    if c1%2==0:
        print(f'{n1}-even')
    if c2%2!=0:
        print(f'{n2}-odd')