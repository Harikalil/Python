class pattern:
    def get2(self):
        self.pattern1=4
        for x in range(self.pattern1+1):
            for y in range(self.pattern1+1):
                print("*",end=" ")
            print()

class triangle(pattern) :
    def get1(self):
        self.pattern1=4
        for x in range(self.pattern1+1):
            for y in range(self.pattern1,x,-1):
                print("",end=" ")
            for y in range(x+1):
                print("*",end=" ")
            print()
            
class triangle1(triangle) :
    def get3(self):
        self.pattern1=4
        for x in range(self.pattern1,-1,-1):
            for y in range(self.pattern1,x,-1):
                print("",end=" ")
            for y in range(x+1):
                print("*",end=" ")
            print()
objetc1=triangle1()
objetc1.get1()
objetc1.get2()
objetc1.get3()