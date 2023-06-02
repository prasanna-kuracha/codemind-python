n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
b=[]
for i in a:
    if k==a.count(i):
        if i not in b:
            b.append(i)
            s=1
if s==1:
    print(*b,end=' ')
else:
    print('-1')