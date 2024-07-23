def reverser():
    name=input("Enter the name : ")
    for x in range(len(name),-1,-1):
        print(name[:x])
    