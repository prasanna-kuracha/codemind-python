n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n,2):
    f=a[i]
    v=a[i+1]
    for i in range(1,v+1):
        b.append(f)
print(*b)
