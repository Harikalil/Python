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

def pattern4():
    name="Hari prasath"
    for x in range(len(name)+1):
        print(name[:x])
