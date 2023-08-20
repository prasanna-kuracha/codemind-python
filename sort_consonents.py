n=input()
n=n.split()
s=''
o='aeiou'
for i in range(len(n)):
    l=[]
    x=n[i]
    for k in range(len(x)):
        if x[k] not in o:
            l.append(ord(x[k]))
    l.sort()
   
    c=0
    for j in range(len(x)):
        if x[j] not in o:
            s=s+chr(l[c])
            c+=1
        else:
            s=s+x[j]
    if i!=len(n)-1:
        s=s+' '
print(s)
            