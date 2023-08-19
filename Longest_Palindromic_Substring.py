n=input()
s=""
for i in range(0,len(n)):
    p=""
    for j in range(i,len(n)):
        p=p+n[j]
        if p==p[::-1]:
            if len(p)>len(s):
                s=p
print(s)