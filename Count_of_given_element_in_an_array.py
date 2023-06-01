n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in a:
    if i==k:
        c=c+1
print(c)        