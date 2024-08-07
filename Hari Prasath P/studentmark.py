class studentmark:
    mark=[]
    def __init__ (self):
        self.name=input("Enter Student Name : ")
        self.rollno=input("Enter your Roll Number : ")
        self.subject=["Tamil","English","Maths","Physics","Chemistry","ComputerScience"]
        for x in range(len(self.subject)):
            self.mark.append(int(input(f"Enter the Mark for {self.subject[x]}:")))
        print(self.mark)

class addandshow(studentmark):
    def __init__(self):
        self.su=0
        for x in self.mark:
            self.su+=x
        print(self.su)
        
class averages(addandshow):
    def __init__ (self):
        self.avg=self.su//6
        print(f'{self.avg}%')
           


object1=studentmark()
object2=addandshow()
object3=averages()