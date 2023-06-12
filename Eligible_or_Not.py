t=int(input())
for i in range(1,t+1):
    x,y,a=map(int,input().split())
    if a>=x and a<y:
        print('YES')
    else:
        print('NO')