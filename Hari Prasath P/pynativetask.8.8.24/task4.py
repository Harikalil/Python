class bankdetails:
    def __init__(self):
        self.name=input("Enter your name : ")
        self.mail=input("Enter your mail : ")
        self.acctyp=input('''
                          1.SAVINGS ACC
                          2.CURRENT ACC 
                          Enter the option(1,2): ''')
        if self.acctyp==1:
            self.acc="SAVINGS ACC"
        else:
            self.acc="CURRENT ACC"
        l=[self.name,self.mail,self.acctyp,self.acc]
        print(l)
        f=open('bankdetails.txt','w')
        f.write(str(l))
        
obj1=bankdetails()
