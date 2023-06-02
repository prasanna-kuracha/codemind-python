def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in a:
    if i==1:
        continue
    else:
        if fun(i)==1 and i<=k:
            c=c+1
print(c)            