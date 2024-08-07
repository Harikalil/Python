
class evenno:
    def getnumber(self,a):
        self.j=[]
        for x in range(a):
            self.number=int(input("Enter the number : "))
            if self.number%2==0:
                if self.number not in self.j:
                    self.j.append(self.number)
            else :
                if self.number not in self.j:
                    self.number+=1
                    self.j.append(self.number)
    def __del__(self):
        print("Memory Deleted!")

a=evenno()
a.getnumber(int(input("Enter the Number Values :")))
print(a.j)
