#File Handling 
path=input("Enter the Path & File name:")
f=open(path,'w')
f.write(input("Enter the name:"))
f.close()

f=open("F:\\Muthu.txt",'a')
f.write(input("enter the name:"))
f.close()


f=open("f.csv",'r')
l=f.read()
print(l)