k = open("INPUT.txt", "r")
f = k.readline().strip()  
k1 = k.readline().strip()
s = f.split()
d = [int(x) for x in s]
t = sum(d)
k = int(k1)
print(d, k)
if k - t:
    oo = open("OUTPUT.txt", "a")
    h1=str(k-t)
    oo.write(h1)
    oo.close()
