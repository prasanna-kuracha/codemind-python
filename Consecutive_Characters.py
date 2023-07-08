n=input()
m=0
for i in range(len(n)):
    c=0
    for j in range(i,len(n)):
        if n[i]==n[j]:
            c=c+1
        else:
            break
    if c>m:
        m=c
print(m)