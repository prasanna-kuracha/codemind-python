n=int(input())
a=list(map(int,input().split()))
m=n//2
p=s=0
for i in range(0,m):
    s=s+a[i]
for i in range(m,n):
    p=p+a[i]
print(abs(s-p))    