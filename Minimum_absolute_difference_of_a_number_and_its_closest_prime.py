def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
for i in range(n,2*n):
    if fun(i)==1:
        x=i
        k=abs(n-x)
        break
for i in range(n,0,-1):
    if fun(i)==1:
        p=i
        m=abs(n-p)
        break
if k==m:
    print(k)
elif k<m:
    print(k)
else:
    print(m)