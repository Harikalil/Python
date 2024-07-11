word1=input("Enter the word 1 : ")
word2=input("Enter the word 2 : ")
l1=list(word1)
l2=list(word2)
l1.sort()
l2.sort()
s=0
for x in range(len(l1)):
    if l1[x]==l2[x]:
        s+=1
if s==len(l1):
    print('anagram')
else:
    print('not a anagram')
 