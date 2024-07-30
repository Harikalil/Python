class pattern :
    def __init__ (self):
        self.pattern=5
        for x in range(self.pattern):
            for y in range (self.pattern):
                if x==0 and y==0 or x==0 and y==4 or x==4 and y==0 or x==4 and y==4:
                    print ("*",end=" ")
                elif x==5//2 and y==5//2:
                    print("0",end=" ")
                else:
                    print(" ",end=" ")
            print()
pattern()