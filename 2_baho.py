k = open("INPUT.txt", "r")
f=int(k.read())
if f >= 38:
    k = f % 10
    s = (f - k) / 10
    if s - k >= 3:
        oo= open("OUTPUT.txt", "a")
        o1=int(s)*10+5
        oo.write(str(o1))
        oo.close()
        print(int(s)*10+5)
        
        
