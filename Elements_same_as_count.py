n=int(input())
a=list(map(int,input().split()))
s=0
b=[]
for i in a:
    if i==a.count(i):
        if i not in b:
            b.append(i)
            s=1
if s==1:
    print(*b,end=" ")
else:
    print('-1')