f1r = open("1.txt") 
f2r = open("2.txt") 

a1 = f1r.read()
a2 = f2r.read()

f1w = open("1.txt","w+")
f2w = open("2.txt","w+")

f1w.write(a2)
f2w.write(a1)