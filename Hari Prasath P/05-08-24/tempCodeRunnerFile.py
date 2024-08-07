h=1000
class Bank:
  
    def getCustomerdetails(self):
        global h
        self.__name=input("Enter the Customer Name:")
        self.__AccountNumber=h
        self.__AccountType=input("Enter the Account Type:")
        h+=1
     

class HouseLoan(Bank):
    def showData1(self):
        print(f'{self.__name}\n{self.__AccountNumber}\n{self.__AccountType}')
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
