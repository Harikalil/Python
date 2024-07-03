#Jump Statement 
''' 
Break - the loop get exit 
Continue - Current Iteration will skip and moves to next iteration 
pass- to denote empty block and no changes will occur on the program 
'''

for x in range(1,11,1):
    if x==4:
        break
    print(x,end=" ")
print()   
for x in range(1,11,1):
    if x==4:
        continue
    print(x,end=" ")
print()
for x in range(1,11,1):
    if x==4:
        pass
    print(x,end=" ")
print()

