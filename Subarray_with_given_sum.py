t=int(input())
for i in range(1,t+1):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s=s+a[j]
            if s==m:
                c=1
                print(i+1,j+1)
        if c==1:
            break
    if c==0:
        print("-1")