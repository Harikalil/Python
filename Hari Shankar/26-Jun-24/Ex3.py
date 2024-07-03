#bit wise Operator

a=int(input("Enter the Number1:"))
b=int(input("Enter the Number2:"))
# print(f'{a}&{b} is {a&b}')#bit wise and 
# print(f'{a}|{b} is{a|b}')#bit wise or 
# print(f'{a}^{b} is {a^b}')#bit wise xor

print(~a)#negation operator
print(a<<5)#left shift
print(b>>1)#right shift


'''
5<<1
   0101     
   1010 

   8421    
5- 0101
7- 0111

10-1010
9 -1001
   1000 - 8

1-0001
2-0010
0-0000   

Bit Wise and - 8
Bit Wise or - 11
Bit Wise xor - 3
'''