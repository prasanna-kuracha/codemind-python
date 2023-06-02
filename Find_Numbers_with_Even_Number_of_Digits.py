def fun(n):
    s=0
    while n!=0:
        r=n%10
        s=s+1
        n=n//10
    if s%2==0:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    l=fun(i)
    if l==1:
        c=c+1
print(c)    