#inheritance 
#is used to extend or inhert the data member and member function 
#single Inheritance
#Base class , Super class  , Parent Class
class Student:
    def getData(self):
        self.Name=input("Enter the Name: ") 
        self.Age=int(input("Enter the Age:"))

#child class , derived class , sub class
class records(Student):
    def showData(self):
        print(f'{self.Name}\t{self.Age}')

r=records()

r.getData()
r.showData()