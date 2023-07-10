n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if a[i]>0:
        x=a[i]
    else:
        x=-a[i]
    p=str(x)
    if len(p)==m:
        b.append(x)
print(len(b))