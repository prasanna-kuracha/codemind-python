n=input()
n=n.split()
x=n[0]
y=list(n[1])
c=0
for i in x:
    for j in y:
        if i==str(j):
            c=c+1
            y.remove(j)
            break
if len(x)==c:
    print(True)
else:
    print(False)
