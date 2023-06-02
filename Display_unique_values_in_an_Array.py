n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for i in a:
    x=a.count(i)
    if x==1:
        s=2
        b.append(i)
if s==2:
    print(*b)
else:
    print('-1')