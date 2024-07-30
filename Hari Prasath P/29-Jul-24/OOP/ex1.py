#List of Object
class Student:
    def getData(self):#self is used to store the current Instance or Memory of the object
        self.Name=input("Enter the Name:")
        self.Age=int(input("Enter the age:"))
    def showData(self):
        print(f'Name:{self.Name}\tAge:{self.Age}')
    
records=[]
no=int(input("Enter the no.of.records"))
for x in range(no):
    records.append(Student())#object creation for the class student
    records[x].getData()
for x in records:
    x.showData()