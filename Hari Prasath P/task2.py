s="this boy is very nice person"
p=""
for x in s.split(" "):
    p=p+x[::-1]+" "
print(p)