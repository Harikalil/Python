name=(input("enter the name:"))
ascii=[]
for x in name:
    ascii.append(ord(x))

for x in range(len(name)):
    print(f'{name[x]}-{ascii[x]}')