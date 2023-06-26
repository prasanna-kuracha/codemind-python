n=int(input())
m=list(map(int,input().split()))
k=1
while 1:
    c=0
    for i in range(len(m)):
        if k%m[i]==0:
            c=c+1
    if c==n:
        print(k)
        break
    k=k+1