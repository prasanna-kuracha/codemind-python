n=input()
n=n.split(":")
h=int(n[0])
m=int(n[1])
a=abs((h*30)-(11/2)*m)
if a<180:
    print(a)
else:
    print(360-a)