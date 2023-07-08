n=input()
b=[]
k='AEIOUaeiou'
for i in range(len(n)):
    if n[i] in k:
        b.append(n[i])
j=len(b)-1
c=[]
for i in range(len(n)):
    if n[i] in k:
        c.append(b[j])
        j=j-1
    else:
        c.append(n[i])
for i in range(len(c)):
    print(c[i],end="")