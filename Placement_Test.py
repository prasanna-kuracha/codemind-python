n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    x=a//10
    y=x*b
    print(y)