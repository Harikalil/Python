x=int(input("Enter the x-axis : "))
y=int(input("Enter the y-axis : "))
if x>=0 and y>=0 :
    print ("It is quadrant 1 in the graph")
elif x<0 and y>=0 :
    print ("It is quadrant 2 in the graph")
elif x<0 and y<0 :
    print ("It is quadrant 3 in the graph")
else :
    print ("It is quadrant 4 in the graph")