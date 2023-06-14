a,b=map(int,input().split())
s=0
for i in range(1,a+1):
    c=list(map(int,input().split()))
    for i in range(0,b):
        s=s+c[i]
print(s)
    