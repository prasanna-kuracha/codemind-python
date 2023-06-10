n=int(input())
for i in range(1,n+1):
    b=int(input())
    a=list(map(int,input().split()))
    c=sum(a)
    k=b*(b+1)//2
    print(k-c)
    