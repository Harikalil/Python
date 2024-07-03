#Logical operators
'''
And Operator 
a   b   a.b
0   0   0
0   1   0
1   0   0
1   1   1

or Operator 
a   b   a+b
0   0   0
0   1   1
1   0   1
1   1   1

not operator
a   not(a)
0   1
1   0

'''

mark=int(input("Enter the Mark:"))
attendance=int(input("Enter the Attendance:"))
print("And-",mark>=35 and attendance>=75)
print("Or-",mark>=35 or attendance>=75)
print("Not-",not(mark>=35 or attendance>=75))