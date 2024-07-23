class student :
    def get(self):
        self.name=input("Enter your name : ")
        self.age=input("Enter your age : ")
        self.bloodgroup=input("Enter the blood group : ")
        self.clsandsec=input("Enter class and section : ")
        self.address=input("Enter the address : ")
        self.mobileno=input("Enter the mobile number : ")
    def show(self):
        print(f'{self.name}\t|{self.age}\t|{self.bloodgroup}\t|{self.clsandsec}\t|{self.address}\t|{self.mobileno}')

object1=student()
object1.get()
object1.show()