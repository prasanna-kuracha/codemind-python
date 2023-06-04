n=int(input())
for i in range(1,n+1):
    g=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if b==a:
        print('0')
    else:
        print(max(b)-min(b))