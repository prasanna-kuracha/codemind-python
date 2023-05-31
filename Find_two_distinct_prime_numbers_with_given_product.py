def fun(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
    
n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        s=i
        if fun(s)==1:
            y=n//s
            if fun(y)==1:
                c=1
                print(s,y)
                break
if c==0:
    print('-1')
    
    