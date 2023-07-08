n=input()
m=0
k='aeiou'
for i in range(len(n)):
    c=0
    for j in range(i,len(n)):
        if n[j] in k:
            c=c+1
        else:
            break
    if c>m:
        m=c
print(m)
        