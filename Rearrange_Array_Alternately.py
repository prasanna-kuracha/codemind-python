n=int(input())
for i in range(1,n+1):
    m=int(input())
    a=list(map(int,input().split()))
    i=0
    j=m-1
    b=[]
    while i<=j:
        b.append(a[j])
        j=j-1
        if a[i] not in b:
            b.append(a[i])
            i=i+1
    print(*b)