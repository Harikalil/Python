'''
Logical Operator 
And
Truth Table 
a   b   a.b
0   0   0
0   1   0
1   0   0
1   1   1

Or
a   b   a+b
0   0   0
0   1   1
1   0   1
1   1   1

Not
a   Not a
0   1
1   0
'''

mark=int(input("Enter the marks:"))
attendance=int(input("Enter the Attendance:"))
print(mark>=35 and attendance>=75)
print(mark>=35 or attendance>=75)
print(not mark>=35)
# print(mark>=35)
# print(attendance>=75)
print(f'{mark}>=35 and {attendance}>=75 is {mark>=35 and attendance>=75}\t{mark>=35 or attendance>=75}\t{not mark>=35 and attendance>=75}')