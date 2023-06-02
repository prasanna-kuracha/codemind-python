def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1       

n=int(input())
a=list(map(int,input().split()))
p=f=1
for i in a:
    if fun(i)==1:
        p=p*i
    else:
        f=f*i
print(abs(p-f))        
        
        