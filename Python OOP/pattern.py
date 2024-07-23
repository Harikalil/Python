def pattern1():
    for x in range(5):
        for space in range(5,x,-1):
            print(" ",end="")
        for y in range(x+1):
            print("*",end=" ")
        print()

def pattern2():
    for x in range(5):
        for y in range(x+1):
            print("*",end=" ")
        print()


def pattern3():
    for x in range(5):
        for y in range(x+1):
            print(y,end=" ")
        print()