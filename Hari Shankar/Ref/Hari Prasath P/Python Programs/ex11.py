unit=int(input("enter the consumed electricity unit:"))
if unit<=50:
    print("the bill for you:",0.50*unit+unit*20/100)
elif unit>=50 and unit<=150:
    print("the bill for you:",0.75*unit+unit*20/100)
elif unit>=150 and unit<=250:
     print("the bill for you:",1.20*unit+unit*20/100)
elif unit>250:
     print("the bill for you:",1.50*unit+unit*20/100)
    