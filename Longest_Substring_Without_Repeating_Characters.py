n=input()
s=""
for i in range(len(n)):
    p=""
    for j in range(i,len(n)):
        k=n[j].upper()
        l=n[j].lower()
        if k not in p and l not in p:
            p=p+n[j]
        else:
            break
    if len(p)>len(s):
        s=p
if len(s)>=3:
    print(s)
else:
    print('-1')