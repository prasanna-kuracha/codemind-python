n=int(input())
s=list(map(int,input().split()))
m=0
for i in range(n):
    if s[i]==1:
        c=0
        for j in range(i,n):
            if s[i]==s[j]:
                c=c+1
            else:
                break
        if c>m:
            m=c
print(m)
    
