n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
c=[]
m=[]
for i in range(0,k):
    b.append(a[i])
for i in range(k,n):
    c.append(a[i])
for i in range(len(b)):
    m.append(b[i])
    m.append(c[i])
print(*m)