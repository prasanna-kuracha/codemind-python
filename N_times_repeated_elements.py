n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
s=0
for i in a:
    if a.count(i)==k:
        if i not in b:
            b.append(i)
            s=1
if s==1:
    print(*b)
else:
    print('-1')
