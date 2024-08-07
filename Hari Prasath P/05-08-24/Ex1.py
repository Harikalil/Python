#multi level inheritance 
class A:
    def getData(self):
        self.Name=input("Enter the Name:")
        self.Role=input("Enter the Role:")
        self.Age=int(input("Enter the Age:"))

class B(A):
    def showData(self):
        print(f'{self.Name}\t{self.Role}\t{self.Age}')
    def salary(self):
        self.salary=int(input("Enter the Salary"))

class C(B):
    def calSalary(self):
        print(f'Monthly Salary:{self.salary} \n Salary per day:{self.salary/30} ')
obj=C()
obj.getData()
obj.showData()
obj.salary()
obj.calSalary()



#multiple inheritance 
class A:
    def getData(self):
        self.Name=input("Enter the Name:")
        self.Role=input("Enter the Role:")
        self.Age=int(input("Enter the Age:"))

class B:
    def showData(self):
        print(f'{self.Name}\t{self.Role}\t{self.Age}')
   
       

class C(A,B):
    def calSalary(self):
        self.salary=int(input("Enter the Salary"))
        print(f'Monthly Salary:{self.salary} \n Salary per day:{self.salary/30} ')
obj=C()
obj.getData()
obj.showData()
obj.calSalary()


#hierarchy Inheritance 

class Bank:
    h=1000
    def getCustomerdetails(self):
        self.name=input("Enter the Customer Name:")
        self.AccountNumber=self.h
        self.AccountType=input("Enter the Account Type:")
        self.h+=1

class HouseLoan(Bank):
    def showData(self):
        print(f'{self.name}\n{self.AccountNumber}\n{self.AccountType}')
        self.op=input("Press Yes to Apply Home Loan:")
        if self.op=="Yes" or self.op=="YES" or self.op=="yes":
            self.loanamount=int(input("Enter the Loan Amount:"))
            print("Thank For Applying Home Loan")

class EducationLoan(Bank):
    def showData(self):
        print(f'{self.name}\n{self.AccountNumber}\n{self.AccountType}')
        self.op=input("Press Yes to Apply Education Loan:")
        if self.op=="Yes" or self.op=="YES" or self.op=="yes":
            self.loanamount=int(input("Enter the Loan Amount:"))
            print("Thank For Applying Education Loan")

obj1=HouseLoan()
obj1.getCustomerdetails()
obj1.showData()
obj2=EducationLoan()
obj2.getCustomerdetails()
obj2.showData()


            

#Hybrid Inheritance 
h=1000
class Bank:
  
    def getCustomerdetails(self):
        global h
        self.name=input("Enter the Customer Name:")
        self.AccountNumber=h
        self.AccountType=input("Enter the Account Type:")
        h+=1
     

class HouseLoan(Bank):
    def showData1(self):
        print(f'{self.name}\n{self.AccountNumber}\n{self.AccountType}')
        self.op=input("Press Yes to Apply Home Loan:")
        if self.op=="Yes" or self.op=="YES" or self.op=="yes":
            self.loanamount=int(input("Enter the Loan Amount:"))
            print("Thank For Applying Home Loan")

class EducationLoan(Bank):
    def showData2(self):
        print(f'{self.name}\n{self.AccountNumber}\n{self.AccountType}')
        self.op=input("Press Yes to Apply Education Loan:")
        if self.op=="Yes" or self.op=="YES" or self.op=="yes":
            self.loanamount=int(input("Enter the Loan Amount:"))
            print("Thank For Applying Education Loan")

class Loan(EducationLoan,HouseLoan):
    pass

l=[]
for x in range(2):
    l.append(Loan())
    l[x].getCustomerdetails()

for x in range(2):
    l[x].showData1()
    l[x].showData2()
