t=int(input())
for k in range(1,t+1):
    n,m=map(int,input().split())
    for i in range(m):
        p=i*i
        if p%m==n:
            print(i)
            break
    else:
        print("-1")
        