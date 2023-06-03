n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n):
    f=1
    for j in range(0,n):
        if i!=j:
            f=f*a[j]
    b.append(f)
print(*b)        