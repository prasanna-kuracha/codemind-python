def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
def fig(k):
    q=k
    s=0
    while q!=0:
        r=q%10
        s=s*10+r
        q=q//10
    if k==s:
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,100000):
    if fun(i)==1 and fig(i)==1 :
        print(i)
        break
        
    