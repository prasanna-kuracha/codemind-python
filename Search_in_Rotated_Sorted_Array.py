n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(a)):
    if a[i]==k:
        c=1
        print(i)
if c==0:
    print("-1")