p=input("Enter the product name : ")
qty=int(input("Enter the quantity of the product :"))
fanprice=int(input("Enter the price of the fan :"))
if p=="fan" :
    print("The price of single fan is ",fanprice,",  The quantity you purchased was :",qty,",The total price is :",fanprice*qty)