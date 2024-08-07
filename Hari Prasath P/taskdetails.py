class details:
    def getdata(self):
        self.name=input("Enter your name : ")
        self.age=int(input("Enter your age : "))
        self.mno=int(input("Enter your mobile number : +91 "))
        self.email=input("Enter your Email : ")
class bankdetails(details):
    def showdata(self):
        print(f'Name : {self.name} \n Age : {self.age} \n Mobile number : +91 {self.mno} \n Email : {self.email} ')

personaldetail=bankdetails()
personaldetail.getdata()
personaldetail.showdata()