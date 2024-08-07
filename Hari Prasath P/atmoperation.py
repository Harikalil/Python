class ATM :
    def __init__(self):
        self.operations=input(''' 1.WITHDRAW
                                  2.DEPOSIT
                                  3.BALANCE CHECK
                              Enter the option : ''')
        if self.operations == 1:
            print("You selected WITHDRAW option")
            amount=input("Enter the amount to be withdrawn : ")
            
            