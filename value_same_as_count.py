n=int(input())
a=list(map(int,input().split()))
s=0
b=[]
for i in a:
    if i==a.count(i):
        if i not in b:
            b.append(i)
            s=s+1
print(s)