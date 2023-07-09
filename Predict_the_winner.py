n=int(input())
a=list(map(int,input().split()))
c=e=0
for i in range(0,n):
    if i%2==0:
        c=c+a[i]
    else:
        e=e+a[i]
s=abs(c-e)
if s%4==0:
    print('X')
else:
    print('Y')
    
    
    