def vowelseperator():
    a=65
    for x in range(65,91,1):
      match x:
        case 65:
          print(chr(x),"--vowel")
        case 69:
          print(chr(x),"--vowel")
        case 73:
          print(chr(x),"--vowel")
        case 79:
          print(chr(x),"--vowel")
        case 85:
          print(chr(x),"--vowel")
        case _:
          print(chr(x),"-- not a vowel")
        





 #calling 
vowelseperator()       