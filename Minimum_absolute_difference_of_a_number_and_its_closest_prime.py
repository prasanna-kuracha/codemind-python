def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
for i in range(n,2*n):
    if fun(i)==1:
        x=i
        y=abs(n-x)
        break
for i in range(n,1,-1):
    if fun(i)==1:
        p=i
        m=abs(n-p) 
        break
if y==m:
    print(y)
elif y<m:
    print(y)
else:
    print(m)
        