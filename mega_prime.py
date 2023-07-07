def fun(n):
    if n==1:
        return 0
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return 0
        return 1
n=int(input())
k=fun(n)
if k==1:
    c=cou=0;
    while n!=0:
        r=n%10
        c=c+1
        if(fun(r)==1):
            cou=cou+1
        n=n//10
    if cou==c:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")