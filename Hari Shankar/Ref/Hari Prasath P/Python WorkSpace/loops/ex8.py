# A=int(input("enter the starting letter:"))

# while True:
#     print(chr(A),end=" ")
#     A+=1
#     if A>90:
#         break
    
start=int(input("Enter the Starting Value:"))
end=int(input("Enter the ending Value:"))
step=int(input("Enter the step:"))
for x in range(start,end,step):
    print(chr(x))
    