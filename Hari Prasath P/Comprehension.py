#Comprehension 
'''
List Comprehension 
Map
Filter 
Lamdba 
Reduce 
'''

fruits=["Apple","Cherry","Mango","Lemon"]

print([x for x in fruits if "o" in x])

jio=["9361886088" ,"8754619879","8778706088","93610586088"]

print([x for x in jio if x.startswith("9") and x.endswith("6088")])


from random import *

for x in range(10):
    print("123456"+str(randint(100000,999999)))
    
from random import *  
for y in range(10):
    str1=""
    for x in range(32):
        str1+=str(randint(0,9))+chr(randint(65,71))
    print(str1)
from random import * 
li=list("225ef0ea5988dc33b491b891e60400220d7c861b9e8f1ccd3b97c3253f1cebbe")
for x in range (10): 
    shuffle(li)
    shuffled_string = ''.join(li)
    print(shuffled_string)
