def fun(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1        
n=int(input())
for i in range(1,n+1):
    k=int(input())
    for i in range(k,0,-1):
        if fun(i)==1:
            f=i
            break
    for i in range(k,2*k):
        if fun(i)==1:
            g=i
            break 
    if abs(k-f)==abs(k-g):
        print(f)
    elif abs(k-f)<abs(k-g):
        print(f)
    else:
        print(g)
        
    