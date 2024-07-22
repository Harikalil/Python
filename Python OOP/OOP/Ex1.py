'''
OOP 

Object 
Object has State , Behaviour & Identity 
<objectname> = <classname>()



Class
Class is a Template , Collection of object 
Class is a user defined datatype 
Class has a data member & member function 
class can have n number of objects
class memory is allocated after the object creation 
class can be access through object 
class data member & member function is always public access specifier 
class method as a default parameter self 
self is used to hold the current memory or instance of the class 

No Underscore - Public 
double Underscore - Private 
single Underscore - protected 

class <classname>:
    //data member 
    //member functions

Constructor & Destructor 

4 Pillar 
Inheritance
Polymorphism
Abstract
Encapsulation 

'''

class student:
    #member function
    def getData(self):
        print(self)
        self.Name=input("Enter the Name:")
        self.Age=int(input("Enter the age:"))
        self.City=input("Enter the city Name:")
    def showData(self):
        print(f'{self.Name}\t{self.Age}\t{self.City}')
        
#obj1=student()
#obj2=student()
#obj1.getData()
#obj2.getData()

#print("--------------")
#obj1.showData()
#obj2.showData()
#print(obj1.Name)

class employee:
    def getdata(self):
        self.name=input("Enter the name : ")
        self.age=input("Enter the age : ")
        self.salary=input("Enter the salary : ")
        self.hometown=input("Enter your Hometown : ")
    def showData(self):
        print(f'{self.name}\t{self.age}\t{self.salary}\t{self.hometown}')


obj1=employee()
obj2=employee()
obj1.getdata()
obj2.getdata()

print("--------------")
obj1.showData()
obj2.showData()

    