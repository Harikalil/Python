class namepattern:
    def __init__(self):
        self.name=input("Enter The Name : ")
        for x in range(len(self.name)):
            for y in range(len(self.name)):
                if x==y or x+y==len(self.name)-1:
                    print(self.name[y],end=" ")
                else:
                    print(" ",end=" ")
            print()
object1=namepattern()