n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for i in a:
    if i==a.count(i):
        if i not in b:
            b.append(i)
print(len(b))
