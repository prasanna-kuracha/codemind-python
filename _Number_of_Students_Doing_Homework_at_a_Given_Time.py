n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if a[i]<=k and b[i]>=k:
        c=c+1
print(c)