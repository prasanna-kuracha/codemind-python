def fun(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
    
a=int(input())
b=int(input())
c=a+b
for i in range(1,c+1):
    x=c+i
    if fun(x)==1:
        print(i,end=" ")
        break;