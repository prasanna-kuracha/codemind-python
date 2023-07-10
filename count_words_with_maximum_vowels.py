n=input()
n=n.split()
v='aeiou'
b=[]
for i in range(len(n)):
    x=n[i]
    c=0
    for i in range(0,len(x)):
        if x[i] in v:
            c=c+1
    b.append(c)
m=max(b)
print(b.count(m))
    