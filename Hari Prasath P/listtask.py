no=int(input("Enter the number names : "))
n=[]
l={}
for x in range (no):
    name=input("Enter the name : ")
    n.append(name)
    if name not in l:
        l[name]=len(name)

print(l)