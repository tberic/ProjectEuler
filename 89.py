f=open("89.txt")
d=""
g=""
s=f.readline()
while(s!=""):
 g=g+s
 s=s.replace("DCCCC", "CM")
 s=s.replace("LXXXX", "XC")
 s=s.replace("VIIII" , "IX")
 s=s.replace("IIII" , "IV")
 s=s.replace("XXXX", "XL")
 s=s.replace("CCCC" , "CD")
 d=d+s
 s=f.readline()
 
print len(g)-len(d)
