k = open("INPUT.txt", "r")
f=int(k.read())
if f%2==0:
    oo= open("OUTPUT.txt", "a")
    oo.write("Second player")
    oo.close()
if f%2==1:
    oo= open("OUTPUT.txt", "a")
    oo.write("First player")
    oo.close()

        
        
