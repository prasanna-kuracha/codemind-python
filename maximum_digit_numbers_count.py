n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    x=str(a[i])
    b.append(len(x))
k=max(b)
c=[]
for i in range(n):
    x=str(a[i])
    if len(x)==k:
        c.append(x)
print(*c)
    