n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for i in a:
    if i==a.count(i):
        if i not in b:
            b.append(i)
            s=1
if s==1:
    k=sum(b)/len(b)
    print(format(k,".2f"))
else:
    print('-1')

    