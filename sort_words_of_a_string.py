n=input()
n=n.split()
s=''
for i in range(len(n)):
    l=[]
    x=n[i]
    for k in range(len(x)):
        v=ord(x[k])
        if v>=90 and v<=122:
            l.append(v)
        elif v>=49 and v<=57:
            l.append(v)
        elif v>=65 and v<=90:
            l.append(v)
    l.sort()
   
    c=0
    for j in range(len(x)):
        if ord(x[j]) in l:
            s=s+chr(l[c])
            c+=1
        else:
            s=s+x[j]
    if i!=len(n)-1:
        s=s+' '
print(s)
            