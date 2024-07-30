class pattern :
    def generate(self,a):
        for x in range(1,a+1):
            print(" "*((a+1)-x),end=" ")
            print("* "*x)
            
p=pattern()
p.generate(10)
            
            
            
