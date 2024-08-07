class employee :
    def empdata(self):
        self.name=input("Enter your name : ")
        self.age=input("Enter the age : ")
        self.experience=int(input("Enter the experience : "))
        self.salary=int(input("Enter your salary : "))
        if self.experience>=5:
            print(f'{self.salary}- Bonus is {self.salary//100*5}')
        else:
            print(f'{self.salary}- Bonus is {self.salary//100*1}')
object=employee()
object.empdata()