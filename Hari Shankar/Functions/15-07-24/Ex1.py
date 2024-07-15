#call by value 
'''
Call by value is define as a copy of value is passed as parameter to the function 
The Value change inside the function for the given parameter will not reflect 
out side the function 
'''
def callvalue(num):
    num=num+100
    print(f'the value of num inside the function is {num}')
num=1
callvalue(num)
print(f'the value of num outside the function is {num}')

#call by reference 
'''
Call by reference is define as a address of the variable is passed as parameter to the function 
the value change inside the function will reflect out side the function 
'''
def mark(num):
    num.append(100)
    print(num)
m=[1,2,3,4,5,6,7,8,9,10]
mark(m)
print(m)


#recursive function 
'''
Function call by itself
'''

def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)
    
print(fact(5))
'''
i=5 5==1    return 5*fact(4)=5*24=120
i=4 4==1    return 4*fact(3)=4*6=24
i=3 3==1    return 3*fact(2)=3*2=6
i=2 2==1    return 2*fact(1)=2*1=2
i=1 1==1    return 1

'''


#optional parameter 
def student(a,b=None):
    print(a,b)

student('Muthu')

#default parameter 
def student(a,b=None,c="James"):
    print(a,b,c)

student('Muthu')

#named parameter 
def student(Name,age):
    print(f'My Name is {Name}')
    print(f'My Age is {age}')
student(age=20,Name='Hari')


# Args parameter 
def show(*i):
    print(list(i))

show(1,2,3,4,5,6,7,8,9,10)


#kwarg parameter
def show(**a):
    print(a)
show(name="hari",age=20)


# import math
# import math as m

from math import *
from random import *

print(pow(2,3))
print(sqrt(16))
print(ceil(5.2))
print(floor(5.5))
print(round(5.5))
print(randint(1000,9999))
print(factorial(5))
print(cos(0))
print(sin(0))
print(abs(-10))

from string import *
for x in ascii_letters:
    print(x,end=" ")
print()
for x in ascii_lowercase:
    print(x,end=" ")
print()
for x in ascii_uppercase:
    print(x,end=" ")
    
from datetime import *
print(datetime.now())
print(datetime.now().date())
print(datetime.now().time())
print(datetime.now().day)
print(datetime.now().hour)