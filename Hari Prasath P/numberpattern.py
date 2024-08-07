class numpattern:
    def pattern(self):
        nrows=int(input("Enter the number of rows : "))
        n=0
        for x in range(nrows+1):
            for y in range(x):
                print(y+1,end=" ")
                if (y+1)%2==0:
                    n+=1
            print()
        print(n)
object=numpattern()
object.pattern()