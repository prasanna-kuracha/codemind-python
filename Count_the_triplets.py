t=int(input())
for i in range(1,t+1):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(i+1,n):
            k=a[i]+a[j]
            if k in a:
                c=c+1
    if c!=0:
        print(c)
    else:
        print('-1')