import pyfiglet

ascii_art = pyfiglet.figlet_format("CREATIVE WALLET CHECKER")
print(ascii_art)

option=input('''
             1.BITCOIN
             2.ETH
             Enter the option of crypto :
             ''')
if option==1:
    print("BITCOIN WALLET CHECKER UNAVAILABL")
else:
    from random import * 
li=list("225ef0ea5988dc33b491b891e60400220d7c861b9e8f1ccd3b97c3253f1cebbe")
gen=int(input("Enter the number private wallet key : "))
for x in range (1,gen+1): 
    shuffle(li)
    shuffled_string = ''.join(li)
    print(x,"--",shuffled_string)
    print()
    f=open("WALLETKEY.txt",'a')
    f.write(str(x)+"--"+shuffled_string+"\n")