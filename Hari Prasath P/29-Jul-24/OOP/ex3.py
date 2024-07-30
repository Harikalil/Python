#constructor is a special type of function 
#which invokes automatically after the object creation 
#__init__
#constructor used to intialize the value during object creation
class pattern :
    def __init__(self,a):
        for x in range(1,a+1):
            print(" "*((a+1)-x),end=" ")
            print("* "*x)
            
q=pattern(5)
print()
p=pattern(10)


class pattern1 :
    def __init__(self):
        self.a=int(input("Enter the No.of.Rows"))
        for x in range(1,self.a+1):
            print(" "*((self.a+1)-x),end=" ")
            print("* "*x)
            
q=pattern1()
l=pattern1()
