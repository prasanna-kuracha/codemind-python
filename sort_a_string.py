x=input()
l=[]
for k in range(len(x)):
    v=ord(x[k])
    if v>=90 and v<=122:
        l.append(v)
    elif v>=49 and v<=57:
        l.append(v)
    elif v>=65 and v<=90:
        l.append(v)
l.sort()
s=''
j=0
for k in range(len(x)):
    w=ord(x[k])
    if w in l:
        s=s+chr(l[j])
        j+=1
    else:
        s=s+x[k]
print(s)