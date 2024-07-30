class employee :
    def getdata(self):
        self.name=input("Enter the name of employee : ")
        self.exp=input("Enter the experience of the employee : ")
        self.salary=input("Enter the salary of the employee : ")
    def showdata(self):
        print(f'Employee name : {self.name}/t Experience of Employee : {self.exp}/t Salary of the Employee : {self.salary}')
        
data=[]
no=int(input("Enter the number of employee : "))
for x in range (no):
    data.append(employee())
    data[x].getdata()
for x in data:
    x.showdata()