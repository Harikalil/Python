'''
#polymorphism - Many & Form 
Runtime Polymorphism / Later Binding / Dynaic Binding 
Compile Time Polymorphism / Static Binding / Early Binding / Function Overloading 
'''

class Student:
    def Add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        elif a!=None:
            print(a)
        else:
            print("Thank You")

S=Student()
S.Add()
S.Add(10,20)
S.Add("Muthu","Kumar")
S.Add(10.5,20.3,30.4)
S.Add(100)


#runtime polymorphism Function Overriding 
class Student:
    def Add(self,a,b):
        print(f'{a}+{b}={a+b}')
class B(Student):
    def Add(self,a,b):
        super().Add(a,b)
        print(f'{a}-{b}={a-b}')
class C(B):
    def Add(self,a,b):
        super().Add(a,b)
        print(f'{a}*{b}={a*b}')
class D(C):
    def Add(self,a,b):
        super().Add(a,b)
        print(f'{a}//{b}={a//b}')

obj=D()
obj.Add(10,30)