sentence=input("Enter the sentence : ")
c=0
for x in sentence.split(" "):
    if x=="is":
        c+=1
print(c)